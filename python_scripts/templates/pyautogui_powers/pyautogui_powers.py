#!/usr/bin/env python3

import pyautogui
print(pyautogui.size())
width, height = pyautogui.size()

print (width)
print (height)

print (pyautogui.position())

# brincadeira com o Paint
pyautogui.moveTo(1136, 594)

pyautogui.click()

pyautogui.dragTo(1000, 650, duration=1.5)
pyautogui.dragTo(1100, 450, duration=0)

pyautogui.dragRel(-300, -150, duration=0.5)

# para usar com o Terminal em Python3 shel: pyautogui.displayMousePosition()
