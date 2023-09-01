from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import  threading

#X:  744 Y:  908 RGB: (126, 161,  65) left
#X:  957 Y:  696 RGB: (151, 180,  78) up
#X: 1181 Y:  915 RGB: (143, 172,  76) right

time.sleep(2)




def resetSide():
    time.sleep(3)
    return int(1)


left = 0
up = 0
right = 0


while keyboard.is_pressed('q') == False:
    if pyautogui.pixelMatchesColor(744,907,(126, 161,  65), tolerance=10) == False and left <= 0 : #left
        pyautogui.press('a')
        print("Left" + str(left))
        left=1
        up-=1
        right-=1
        #left = int(threading.Thread(target=resetSide()).start())
    elif pyautogui.pixelMatchesColor(957,696,(151, 180,  78), tolerance=10) == False and up <= 0: #up
        pyautogui.press('w')
        print("up" + str(up))
        up=1
        left-=1
        right-=1
        #up = int(threading.Thread(target=resetSide()).start())
    elif pyautogui.pixelMatchesColor(1181,907,(143, 172,  76), tolerance=10) == False and right <= 0: #right
        pyautogui.press('d')
        print("right" + str(right))
        right=1
        left-=1
        up-=1
        #right = int(threading.Thread(target=resetSide()).start())
