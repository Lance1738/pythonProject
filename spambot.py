# TO STOP THE PROGRAM, PRESS THE STOP BUTTON ON THE SCREEN
# TO STOP THE PROGRAM, PRESS THE STOP BUTTON ON THE SCREEN
# TO STOP THE PROGRAM, PRESS THE STOP BUTTON ON THE SCREEN

import pyautogui
import time


def spam():

    msg = input("What do you want to spam? ")
    times = input("How many times do you want to spam? (Leave it blank if you want it to run forever) ")
    if times == '':
        times = 999999999999999999999

    time.sleep(1) # Delay before the program runs. Feel free to change the delay.

    for i in range(int(times)):
        pyautogui.typewrite(msg)
        pyautogui.press('enter')


spam()
