# Sending a String from the Keyboard
import pyautogui
pyautogui.click(100, 200); pyautogui.write('Hello, world!')

# Key Names
pyautogui.write(['a', 'b', 'left', 'left', 'X', 'Y'])

# Pressing and Releasing the Keyboard
pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')

# Hotkey Combinations
pyautogui.keyDown('ctrl')
pyautogui.keyDown('c')
pyautogui.keyUp('c')
pyautogui.keyUp('ctrl')

# Instead, use the pyautogui.hotkey() function,which takes multiple keyboard key 
# string arguments, presses them in order, and releases them in the reverse order.
pyautogui.hotkey('ctrl', 'c')

# Setting Up Your GUI Automation Scripts
import pyautogui
pyautogui.sleep(3)  # Pauses the program for 3 seconds.
pyautogui.countdown(10)  # Counts down over 10 seconds.

print('Starting in ', end=''); pyautogui.countdown(3)