import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# adds text to the image thats repeated upto four times on diffrent lines
def add_text(original_image, text = "Menacing!!"):

    edited_image = original_image.resize((round(original_image.width * 1.5), round(original_image.height * 1.5)), resample=0)
    # (x,y) coordinates for the four lines
    list_opsitions = ((edited_image.width/5, edited_image.height/5),(edited_image.width/2.5, edited_image.height/2.5), 
                      (edited_image.width/2, edited_image.height/2),(edited_image.width/1.5, edited_image.height/1.5))
    
    color_of_text = (106,45,102)
    font_size = int(edited_image.width * 0.059)
    font = ImageFont.truetype(r"font\SF-Fedora.ttf", font_size)
    draw_text = ImageDraw.Draw(edited_image)
    for number_of_lines in range(0,4):
       draw_text.text(list_opsitions[number_of_lines], text, font=font, fill=color_of_text)

    return edited_image

# fades the image to black the closer it is to the corners (used in the filter function)
def fade(image):
    gradient_bottom = Image.new('L', image.size)
    gradient_left = Image.new('L', image.size)
    gradient_right = Image.new('L', image.size)
    gradient_top = Image.new('L', image.size)
    width, height = image.size
    draw_bottom = ImageDraw.Draw(gradient_bottom)
    draw_right = ImageDraw.Draw(gradient_right)
    draw_left = ImageDraw.Draw(gradient_left)
    draw_top = ImageDraw.Draw(gradient_top)
    # to make it brighter
    multiplier = 2.7
    # to make sure it only affects half the image
    division = 2 
    for y in range(int(height / division)):
        brightness = int(255 * (y / height))
        draw_bottom.line((0, (height - y), width, (height - y)), fill=int(brightness * multiplier))
    for y in range(int(height / division)):
        brightness = int(255 * (y / height))
        draw_top.line((0, y, width, y), fill=int(brightness * multiplier))
    for x in range(int(width / division)):
        brightness = int(255 * (x / width))
        draw_left.line((x, 0, x, height), fill=int(brightness * multiplier))
    for x in range(int(width / division)):
        brightness = int(255 * (x / width))
        draw_right.line(((width - x), 0, (width - x), height), fill=int(brightness * multiplier))
    combine_gradient_1 = Image.blend(gradient_bottom, gradient_top, alpha=0.5)
    combine_gradient_2 = Image.blend(gradient_right, gradient_left, alpha=0.5)
    combine_gradients = Image.blend(combine_gradient_1, combine_gradient_2, alpha=0.5)
    image.putalpha(combine_gradients)

    return image
# adds to be continued in the shape of an arrow to the bottom right of the image (for the add filter function)
def add_to_be_continued(image):
    # points for the body of the arrow
    start_xy = (image.width * 0.1, image.height * 0.88)
    end_xy = (image.width * 0.32, image.height * 0.92)
    # points for the small pieces the body of the arrow
    list_start_points = (start_xy, (end_xy[0] * 1.03, start_xy[1] * 0.992), (end_xy[0] * 1.09, start_xy[1] * 1.009))
    list_end_points = (end_xy, (end_xy[0] * 1.06, end_xy[1] * 0.996), (end_xy[0] * 1.12, start_xy[1] * 1.06))
    
    draw = ImageDraw.Draw(image)
    # draws the outline of the body of the arrow
    draw.rectangle(((start_xy[0] * 0.99, start_xy[1] * 0.994), (end_xy[0] * 1.19, end_xy[1] * 1.01)), fill=(88,85,69))
    # draw the head of the arrow
    triangle_points = [(start_xy[0] * 0.5, start_xy[1] + ((end_xy[1] - start_xy[1])/1.9)), (start_xy[0] * 1.25, start_xy[1] / 1.023 ),
                       (start_xy[0] * 1.25, start_xy[1] * 1.08)]
    draw.polygon(triangle_points, fill=(88,85,69))
    triangle_points = [(start_xy[0] * 0.7, start_xy[1] + ((end_xy[1] - start_xy[1])/1.9)), (start_xy[0] * 1.2, start_xy[1] / 1.015 ),
                       (start_xy[0] * 1.2, start_xy[1] * 1.06)]
    draw.polygon(triangle_points, fill=(196,188,175))

    # draws the main (lighter) part the body of the arrow
    for x in range(0, len(list_start_points)):
        draw.rectangle((list_start_points[x], list_end_points[x]), fill=(196,188,175))
    
    # adds the text to the arrow
    text_start = (start_xy[0], start_xy[1] * 1.017)
    font_size = (end_xy[0] - start_xy[0]) * 0.11
    font = ImageFont.truetype(r"font\SF-Fedora.ttf", font_size)
    draw.text(text_start, "To Be Continued", font=font, fill=(88,85,69))
    return image
#the part that will be called in main
def add_filter(original_image):
    edited_image = original_image
    edited_image = edited_image.convert("RGBA")
    edited_image = edited_image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    edited_image = edited_image.filter(ImageFilter.SHARPEN)
    color_of_filter = Image.new("RGBA", edited_image.size,color=(208, 200, 99, 255))
    blended_image = Image.blend(edited_image, color_of_filter, alpha=0.6)
    blended_image = fade(blended_image)
    fully_edited_image = add_to_be_continued(blended_image)
    
    return fully_edited_image