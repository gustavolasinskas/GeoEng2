#! Python3

import pyautogui

pyautogui.screenshot('/users/alex/desktop/screenshot_example.png')
calc7key = pyautogui.locateOnScreen('/users/alex/desktop/calc7key.png')
print (calc7key)

calc7key_center = pyautogui.locateCenterOnScreen('/users/alex/desktop/calc7key.png')
print (calc7key_center)

pyautogui.moveTo(calc7key_center)
pyautogui.moveRel(-40, -20)
pyautogui.click()
