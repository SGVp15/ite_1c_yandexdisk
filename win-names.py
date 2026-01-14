import time

import pyautogui

while True:
    print(f'{pyautogui.getAllTitles()}\t\t\t\t\n\n', end='\r')
    time.sleep(1)
