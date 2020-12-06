#--keyboard_control_success 파일을 토대로 조종이 가능하도록 변형시키는 파일

from pynput import keyboard
from pymavlink import mavutil

def on_press(key):
    print('key %s pressed' % key)

def arm_and_takeoff(altitude):
    altitude > 0
    print('take off')

def on_release(key):
    if key == keyboard.Key.esc:
        return False

if on_press(key='t'):
    key == keyboard.key.t
    arm_and_takeoff(10)

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()
