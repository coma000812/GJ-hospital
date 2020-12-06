# GJ-hospital

import pyautogui
import time

pyautogui.typewrite("cd PX4-Autopilot",interval=0.1)
pyautogui.press('Enter')
time.sleep(1)
pyautogui.press('Enter')
time.sleep(2)
pyautogui.typewrite("make px4_sitl_default gazebo",interval=0.1)
pyautogui.press('Enter')
time.sleep(1)
pyautogui.typewrite("commander takeoff",interval=0.1)
