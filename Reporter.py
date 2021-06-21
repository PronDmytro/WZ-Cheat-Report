import keyboard

import time


def start():
    counter = 0

    while True:
        if keyboard.is_pressed('f9'):
            break
        keyboard.send("X")
        time.sleep(0.05)
        keyboard.send("S")
        time.sleep(0.05)
        keyboard.send("space")
        time.sleep(0.05)
        keyboard.send("space")
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
