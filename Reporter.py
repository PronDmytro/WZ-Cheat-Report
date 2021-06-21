import keyboard
import pyautogui
from pynput.mouse import Button, Controller
import time


def start():
    button = Button.left
    mouse = Controller()
    counter = 0
    while True:
        if keyboard.is_pressed('f9'):
            break
        keyboard.send("X")
        pyautogui.click(673, 491)
        mouse.click(button)
        time.sleep(0.006)
        pyautogui.click(744, 554)
        mouse.click(button)
        time.sleep(0.006)
        counter += 1
    print(counter)
    print("Stop")


if __name__ == '__main__':
    print("WARZONE cheat report clicker\n"
          "by NiNjA_CaT\n"
          "F8 - start\n"
          "F9 - stop\n"
          "F7 - exit\n\n")
    time.sleep(5)
    while True:
        if keyboard.is_pressed('f8'):
            print("Start")
            start()
        elif keyboard.is_pressed('f7'):
            print("Close")
            exit(0)