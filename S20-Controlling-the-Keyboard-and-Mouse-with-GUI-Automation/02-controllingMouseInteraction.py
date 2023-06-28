# Clicking the Mouse
import pyautogui
pyautogui.click(10, 5)  # Move mouse to (10, 5) and click.

# Scrolling the Mouse
pyautogui.scroll(200)

# The MouseInfo application’s window
import pyautogui
pyautogui.mouseInfo()

# Getting a Screenshot
import pyautogui
im = pyautogui.screenshot()

# Analyzing the Screenshot
import pyautogui
pyautogui.pixel((0, 0))

pyautogui.pixel((50, 200))

import pyautogui
pyautogui.pixel((50, 200))

pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))
pyautogui.pixelMatchesColor(50, 200, (255, 135, 144))

# Image Recognition
import pyautogui
b = pyautogui.locateOnScreen('submit.png')
b

b[0]

b.left

# There will be one four-integer tuple for each location where the image is found on the screen.
list(pyautogui.locateAllOnScreen('submit.png'))

# Once you have the four-integer tuple for the specific image you want to
# select, you can click the center of this area by passing the tuple to click().
pyautogui.click((643, 745, 70, 29))

# As a shortcut, you can also pass the image filename directly to the click() function:
pyautogui.click('submit.png')

# Remember locateOnScreen() raises an exception if it can’t find the
# image on the screen, so you should call it from inside a try statement:
try:
    location = pyautogui.locateOnScreen('submit.png')
except:
    print('Image could not be found.')