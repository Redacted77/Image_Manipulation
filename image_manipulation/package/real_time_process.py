import cv2 as cv
import numpy as np

name_of_window = 'real time'
# resizes the image to fit the window
def check_size(image):
    (h, w) = image.shape[:2]
    new_width = int(w * 0.8)
    new_height = int((new_width * 0.75))
    resized_image = cv.resize(image, (new_width, new_height))
    return resized_image
# draws a 3 broken zigzag to mimic lightning
def broken_zigzag(image):
    start_points = [image.shape[1] // 2, image.shape[0] // 2]
    num_of_breaks = 7
    step_size = 100
    up = True
    break_value = 2
    for i in range(num_of_breaks):
        end_x = start_points[0] + step_size
        if i == 2 or i == 6:
            end_y = start_points[1] + step_size * break_value
            cv.line(image, start_points, (end_x, end_y), (0, 255, 255), 3)
            up = not up
            start_points[0], start_points[1] = end_x, end_y
            continue
        end_y = start_points[1] - step_size if up else start_points[1] + step_size
        cv.line(image, start_points, (end_x, end_y), (0, 255, 255), 3)
        up = not up
        start_points[0], start_points[1] = end_x, end_y
    start_points = [image.shape[1] // 2, image.shape[0] // 2]
        
    for i in range(num_of_breaks):
        end_x = start_points[0] - step_size
        if i == 3 or i == 5:
            end_y = int(start_points[1] - step_size * (break_value + 0.5))
            cv.line(image, start_points, (end_x, end_y), (0, 255, 255), 3)
            up = not up
            start_points[0], start_points[1] = end_x, end_y
            continue
        end_y = start_points[1] - step_size if up else start_points[1] + step_size
        cv.line(image, start_points, (end_x, end_y), (0, 255, 255), 3)
        up = not up
        start_points[0], start_points[1] = end_x, end_y
    start_points = [image.shape[1] // 2, image.shape[0] // 2]

    for i in range(num_of_breaks):
        end_x = start_points[0] - step_size
        if i == 1 or i == 4:
            end_y = start_points[1] - step_size * break_value
            cv.line(image, start_points, (end_x, end_y), (0, 255, 255), 4)
            up = not up
            start_points[0], start_points[1] = end_x, end_y
            continue
        end_y = start_points[1] + int(step_size * (break_value + 1)) if up else start_points[1] - step_size
        cv.line(image, start_points, (end_x, end_y), (0, 255, 255), 4)
        up = not up
        start_points[0], start_points[1] = end_x, end_y

    return image
# draws 3 circles in the center of the image
def center_circle(image):
    copy = image.copy()
    cv.circle(image, (image.shape[1] // 2, image.shape[0] // 2), 0, (255, 255, 255), 130)
    image = broken_zigzag(image)
    cv.circle(image, (image.shape[1] // 2, image.shape[0] // 2), 0, (0, 255, 255), 20)
    cv.circle(copy, (image.shape[1] // 2, image.shape[0] // 2), 0, (255, 255, 255),225)
    combine = cv.addWeighted(copy, 0.5, image, 1 - 0.5, 0)

    return combine
# draws 2 solid color lines in the center of the image
def solid_color_column(image):
    cv.line(image, (image.shape[1] // 2, 0), (image.shape[1] // 2, image.shape[0]) , (0, 255, 255), 100)
    cv.line(image, (image.shape[1] // 2, 0), (image.shape[1] // 2, image.shape[0]) , (255, 255, 255), 15)

    return image
# draws a big transparent line then blurs it in the center
def transparent_column(image):
    glow_yelloow_layer = image.copy()
    cv.line(glow_yelloow_layer, (image.shape[1] // 2, 0), (image.shape[1]//2, image.shape[0]), (50, 255, 255),225)
    blurred = cv.GaussianBlur(glow_yelloow_layer, (15, 15), 0)
    transparent_image = cv.addWeighted(blurred, 0.5, image, 1 - 0.5, 0)

    return transparent_image
# a filter that gets darker near the edges, spreads out in the shape of a circle(gives the illusion of light)
def fade_to_black(image):
    (h, w) = image.shape[:2]
    mask = np.zeros((h, w), dtype="float32")
    for i in range(h):
        for j in range(w):
            distance = np.sqrt((i - h / 2) ** 2 + (j - w / 2) ** 2)
            mask[i, j] = 1 - min(1, distance / (np.sqrt((h / 2) ** 2 + (w / 2) ** 2)))
    mask = np.dstack([mask] * 3)
    faded_image = (image * mask).astype("uint8")

    return faded_image
# used in intro function as a sendoff (acts almost the same as the broken zigzag function)
def outro(image):
    copy = image.copy()
    break_value = 2
    for n in range(2):
        alpha = 0.6
        start_points = [image.shape[1] // 2, image.shape[0] // 2]
        num_of_breaks = 7
        step_size = 100
        up = True
        for i in range(num_of_breaks):
            end_x = start_points[0] + step_size
            if i == 2 or i == 6:
                end_y = int(start_points[1] + step_size * break_value)
                cv.line(image, start_points, (end_x, end_y), (0, 255, 255), 3)
                up = not up
                start_points[0], start_points[1] = end_x, end_y
                continue
            end_y = start_points[1] - step_size if up else start_points[1] + step_size
            cv.line(image, start_points, (end_x, end_y), (0, 255, 255), 3)
            up = not up
            start_points[0], start_points[1] = end_x, end_y
        start_points = [image.shape[1] // 2, image.shape[0] // 2]
            
        for i in range(num_of_breaks):
            end_x = start_points[0] - step_size
            if i == n or i == 5:
                end_y = int(start_points[1] - step_size * (break_value + 0.5))
                cv.line(image, start_points, (end_x, end_y), (0, 255, 255), 3)
                up = not up
                start_points[0], start_points[1] = end_x, end_y
                continue
            end_y = start_points[1] - step_size if up else start_points[1] + step_size
            cv.line(image, start_points, (end_x, end_y), (0, 255, 255), 3)
            up = not up
            start_points[0], start_points[1] = end_x, end_y
        start_points = [image.shape[1] // 2, image.shape[0] // 2]

        for i in range(num_of_breaks):
            end_x = start_points[0] - step_size
            if i == n or i == 5:
                end_y = start_points[1] - step_size * break_value
                cv.line(image, start_points, (end_x, end_y), (0, 255, 255), 4)
                up = not up
                start_points[0], start_points[1] = end_x, end_y
                continue
            end_y = start_points[1] + int(step_size * (break_value)) if up else start_points[1] - step_size
            cv.line(image, start_points, (end_x, end_y), (0, 255, 255), 4)
            up = not up
            start_points[0], start_points[1] = end_x, end_y
        start_points = [image.shape[1] // 2, image.shape[0] // 2]
        for i in range(6):
            combine = cv.addWeighted(image, alpha, copy, 1 - alpha, 0)
            cv.imshow(name_of_window, combine)
            cv.waitKey(30)
            alpha = alpha - 0.1
        image = copy.copy()
        break_value = 3
# a pseudo intro animation
def intro(image):
    edited_image = image.copy()
    big_circle = image.copy()
    start_points = [edited_image.shape[1], 0]
    num_of_breaks = 9
    step_size = 80
    up = True
    speed = 70
    for i in range(num_of_breaks):
        end_x = start_points[0] - step_size
        if i == 2 or i == 6:
            end_y = int(start_points[1] + step_size * 3)
            cv.line(edited_image, start_points, (end_x, end_y), (0, 255, 255), 3)
            edited_image = cv.addWeighted(edited_image, 0.6, image, 1 - 0.6, 0)
            cv.imshow(name_of_window,edited_image)
            cv.waitKey(speed)
            up = not up
            start_points[0], start_points[1] = end_x, end_y
            continue
        end_y = start_points[1] + step_size if up else start_points[1] - step_size
        #circle
        if i == num_of_breaks - 1:
            cv.line(edited_image, start_points, (edited_image.shape[1] // 2, edited_image.shape[0] // 2), (0, 255, 255), 3)
            cv.circle(edited_image, (edited_image.shape[1] // 2, edited_image.shape[0] // 2), 0, (255, 255, 255), 20)
            edited_image = cv.addWeighted(edited_image, 0.8, image, 1 - 0.8, 0)
            cv.imshow(name_of_window, edited_image)
            cv.waitKey(speed)
            for i in range(2, 12):
                cv.circle(big_circle, (edited_image.shape[1] // 2, edited_image.shape[0] // 2), 10 * (i * i) , (10 * i, 255, 255), 100)
                big_circle = cv.addWeighted(big_circle, 0.4, image, 1 - 0.4, 0)
                cv.imshow(name_of_window, big_circle)
                cv.waitKey(int(speed * 0.3))
                outro(big_circle) if i == 11 else None
            continue
        cv.line(edited_image, start_points, (end_x, end_y), (0, 255, 255), 3)
        edited_image = cv.addWeighted(edited_image, 0.5, image, 1 - 0.5, 0)
        cv.imshow(name_of_window,edited_image)
        cv.waitKey(speed)
        up = not up
        start_points[0], start_points[1] = end_x, end_y

    return image
# the images that will be displayed once correct order function ends
def final_version(image, conditon_number):
    if conditon_number == 0:
        layer_1 = solid_color_column(image)
        layer_2 = center_circle(layer_1)
        layer_3 = transparent_column(layer_2)
        result = fade_to_black(layer_3)
        return result
    elif conditon_number == 1:
        layer_1 = solid_color_column(image)
        layer_2 = center_circle(layer_1)
        layer_3 = transparent_column(layer_2)
        return layer_3
# display order
def correct_order(original_image, image, number_of_layer):
    if number_of_layer == 1:
        layer_1 = intro(image)
        return layer_1
    elif number_of_layer == 2:
        layer_2 = center_circle(image)
        return layer_2
    elif number_of_layer == 3:
        layer_3 = final_version(original_image, 1)
        return layer_3
    else:
        return image
# fades 2 images together
def fade_in_and_out(final_image, end_image):
    white = np.ones_like(final_image) * 255
    num_of_frames = 60
    for x in range(1, 3):
        for i in range(num_of_frames):
            alpha = i / num_of_frames
            fade_out = cv.addWeighted(final_image, 1 - alpha, white, alpha, 0)
            fade_in = cv.addWeighted(white, 1 - alpha, end_image, alpha, 0)
            transition_frame = fade_out if x == 1 else fade_in
            cv.imshow(name_of_window, transition_frame)
            cv.waitKey(50)
# red filter
def blood_red(image):
    red_filter = np.zeros_like(image)
    red_filter[:, :, 2] = 255
    image = cv.addWeighted(image, 1 - 0.5, red_filter, 0.5, 0)
    image = fade_to_black(image)
    return image
#the part that will be called in main
def real_time_effect(image = cv.imread(r"saved_images\RealTime_default.jpg")):
    end_image = cv.imread(r"saved_images\final_attack.jpg")
    resized_image = check_size(image)
    copy = resized_image.copy()
    final_image = final_version(resized_image.copy(), 0)
    height, width, _ = final_image.shape
    end_image = cv.resize(end_image, (width, height))
    end_image = blood_red(end_image)
    cv.imshow(name_of_window, resized_image)
    cv.waitKey(0)
    for i in range(1,5):
        if i == 4:
            cv.imshow(name_of_window, final_image)
            cv.waitKey(250)
            break
        resized_image = correct_order(copy, resized_image, i)
        cv.imshow(name_of_window, resized_image)
        cv.waitKey(65) if i == 2 or i == 3 else cv.waitKey(250)
    cv.waitKey(0)
    fade_in_and_out(final_image, end_image)
    cv.waitKey(100)
    cv.destroyAllWindows