""" THIS AUTOMATION SCRIPT IS DESIGN FOR KEEP MACHINE AWAKE FOREVER
EXAMPLE : INFINITE BACKLIGHT TIME """

import time
import pyautogui
import schedule


def Move_Left():
    pyautogui.moveTo(900, 500, duration=1)
    pyautogui.press('shift')


def Move_Right():
    pyautogui.moveTo(200, 500, duration=1)
    time.sleep(60)
    pyautogui.press('shift')


def Loop():
    try:
        schedule.every(1).minute.do(Move_Left)
    except Exception as obj:
        print("Exception Occurred : ", obj)
    while True:
        schedule.run_pending()


schedule.every(1).minute.do(Move_Right)
while True:
    Loop()
