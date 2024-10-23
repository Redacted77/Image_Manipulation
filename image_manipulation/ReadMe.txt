Image manipulation
is separated into 3 files first is main.py second is save image process.py third is real time process.py.
the last 2 are in packages, all saved images + the default images are in saved-images and the fonts used are in font.
-main.py
all main does is, based on user input, chooses how and what to run from second or third.

- save image process (uses PIL)

it mainly works by editing an image, saving it then opening it to show it.
*there are 2 main functions in it, add-text which adds text 4 times in a row in a downwards slope, the distance varies.
*add-filter adds a filter similar to (to be continued) filter present in the endings in some episodes of jojo's bizarre adventure.

- real time process (uses CV2)

nothing is saved once the process ends there is nothing left.
it uses cv2 windows to display the image while editing it in real time (making a loop to keep updating cv2.imshow() function).
every effect that this process does is its own function, most is used in correct order function (display order).
aims to make an effect similar to titan shifters lightning transformation, from attack on titan.

*there is 1 main function, real-time-effect it makes use of all other functions in a for loop.
-note worthy function

*final-version function works to fix a problem, of the program taking too much time to display the updated image destroying the real time effect, so it makes the main process of editing the image (in it's actual order) start, before displaying anything, making the display of the last updated image much faster.

*intro makes a pseudo animation for an intro, it also returns the originally given image, as in everything it does gets undone by the time it finishes.

*broken zigzag function works to mimic lightning, by drawing a zigzag, that it keeps breaking, using a if condition as well as multiplying the step value with a variable, called break value.