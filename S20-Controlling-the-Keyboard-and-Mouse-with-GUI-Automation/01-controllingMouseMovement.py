import pyautogui
wh = pyautogui.size() # Obtain the screen resolution.
wh

wh[0]

wh.width

# Moving the Mouse
import pyautogui
for i in range(10):  # Move mouse in a square.
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)

# The following example moves the mouse in the same square pattern,
# except it begins the square from wherever the mouse happens to be 
# on the screen when the code starts running:
import pyautogui
for i in range(10):
    pyautogui.move(100, 0, duration=0.25)   # right
    pyautogui.move(0, 100, duration=0.25)   # down
    pyautogui.move(-100, 0, duration=0.25)  # left
    pyautogui.move(0, -100, duration=0.25)  # up

# Getting the Mouse Position
pyautogui.position()  # Get current mouse position.    

pyautogui.position()  # Get current mouse position again.

p = pyautogui.position()  # And again.
p

p[0]  # The x-coordinate is at index 0.

p.x  # The x-coordinate is also in the x attribute.