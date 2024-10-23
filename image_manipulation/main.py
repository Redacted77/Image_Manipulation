import os
import random
import time
from package import add_text, add_filter, real_time_effect
from PIL import Image

def cool_intro_message():
    words = ["attack on titan", "Kono Dio Da"]
    message = "image manipulation"
    width = 10
    empty_space = int(width / 2)
    for x in range(width):
        num_of_hashes = width - x
        if x >= width // 2:
            if x == width//2:
                ran = random.randint(0, 1)
                space = int((width*2 + empty_space )//6.5)
                for l in range(len(message)):
                    print("\r", end="", flush=True)
                    print(" " * space + words[ran][:l], end="", flush=True)
                    print(message[l], end="", flush=True)
                    time.sleep(0.3/2)
                for n in range(len(message)):
                    print("\r", end="", flush=True)
                    print(" " * space + message[:n], end="", flush=True)
                    time.sleep(0.3/2)
                print("\r", end="", flush=True)
                print(" " * space + message, end="", flush=True)
                print("")
            num_of_hashes = x + 1
            print("#" * (num_of_hashes) + " " * (width*2 - empty_space-2) +  "#" * (num_of_hashes))
            empty_space = empty_space + 2
        else:
            print("#" * (num_of_hashes) + " " * (empty_space + x * 2) +  "#" * (num_of_hashes))
            time.sleep(0.5)
# calls the necessary function, saves and shows the image both before and after
def image_save_handling(img = Image.open(r"saved_images\Default.jpg")):
    print("showing the before image, please wait...")
    img.show("before")
    time.sleep(3)
    while(True):
        user_choice = input("""1.Add text to the image     |||     2.Add a very specific filter\n""")
        # add text
        if user_choice == '1':
            while(True):
                user_given_text = input("Enter text to display (or press 1 to skip): ")
                # makes sure the text isn't too big so it can be displayed properly
                if len(user_given_text) > 8:
                    print("Error: can't be longer than 8 characters")
                elif user_given_text == '1': 
                    result = add_text(img)
                    print("saving image, please wait...")
                    result.save(r"saved_images\text_edited_image.png")
                    print("opening image, please wait...")
                    result.show("after")
                    break
                else:
                    result = add_text(img, user_given_text)
                    print("saving image, please wait...")
                    result.save(r"saved_images\text_edited_image.png")
                    print("opening image, please wait...")
                    result.show("after")
                    break
            break
        # add filter
        elif user_choice == '2':
            result = add_filter(img)
            print("saving image, please wait...")
            result.save(r"saved_images\filter_edited_image.png")
            print("opening image, please wait...")
            result.show("after")
            break
        else:
            print("Error: select a valid option")
# loops the options for the save image process
def first_choice():
    while(True):
        image_path = input("enter image directory or press 1 to go with the default: ")
        if image_path == '1':
            image_save_handling()
            break
        elif os.path.exists(image_path):
            user_image = Image.open(image_path)
            image_save_handling(user_image)
            break
        else:
            print('''Error: Check file path, remove " " and try again''')
# the main part
while(True):
    cool_intro_message()
    while(True):
        user_choice = input("""1.Edit image and save it     |||     2.Edit image in real time and exit\n""")
        if user_choice == '1':
            first_choice()
            break
        elif user_choice == '2':
            print("once the window opens press, any key to start the effect")
            print("when the effect stops press, any key to continue\nthe window will close on it's own, when it's done")
            break
        else:
            print("Error: select a valid option")
    if user_choice == '2':
        break
    end = input("Exit? Y/N\n")
    if end.lower() == 'y':
        exit()
# real time effect freezes if it's inside of the loop (idk why)
real_time_effect()
exit()