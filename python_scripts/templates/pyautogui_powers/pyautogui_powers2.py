#! Python3

import pyautogui

pyautogui.click(100, 300); pyautogui.typewrite('Hello World!\n\n')
pyautogui.hotkey("'", "C")
#pyautogui.hotkey("command", "o")


list_of_keys = pyautogui.KEYBOARD_KEYS

for key in list_of_keys:
    print (key)
