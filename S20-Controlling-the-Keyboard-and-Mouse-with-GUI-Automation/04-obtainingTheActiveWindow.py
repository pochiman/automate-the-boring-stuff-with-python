import pyautogui
fw = pyautogui.getActiveWindow()
fw

str(fw)

fw.title

fw.size

fw.left, fw.top, fw.right, fw.bottom

fw.topleft

fw.area

pyautogui.click(fw.left + 10, fw.top + 20)

# Manipulating Windows
import pyautogui
fw = pyautogui.getActiveWindow()
fw.width  # Gets the current width of the window.

fw.topleft  # Gets the current position of the window.

fw.width = 1000  # Resizes the width.
fw.topleft = (800, 400)  # Moves the window.

# You can also find out and change the window’s minimized, maximized, and activated states.
import pyautogui
fw = pyautogui.getActiveWindow()
fw.isMaximized  # Returns True if window is maximized.

fw.isMinimized  # Returns True if window is minimized.

fw.isActive     # Returns True if window is the active window.

fw.maximize()   # Maximizes the window.
fw.isMaximized

fw.restore()    # Undoes a minimize/maximize action.
fw.minimize()   # Minimizes the window.
import time
# Wait 5 seconds while you activate a different window:
time.sleep(5); fw.activate()
fw.close()      # This will close the window you're typing in.