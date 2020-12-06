#--코드를 실핼 시켰을 시에 "sasdasdasda"가 쳐짐

from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(2)

for char in "sasdasdasda":
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.12)
   
