import os
import time
import pyautogui

os.system("code")
time.sleep(5)

pyautogui.hotkey('ctrl','n')
time.sleep(1)
python_code ="""\
print("Hello World!")
"""
pyautogui.typewrite(python_code,interval=0.05)
pyautogui.hotkey('ctrl','s')
time.sleep(1)
pyautogui.typewrite("hello.py")
pyautogui.press('enter')
