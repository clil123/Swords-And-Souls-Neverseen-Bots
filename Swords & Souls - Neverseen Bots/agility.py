from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)


#X: 1283 Y:  695 RGB: (253, 234, 183) down left
#X: 1287 Y:  541 RGB: (254, 236, 181) mid left
#X: 1542 Y:  519 RGB: (253, 236, 180) up left
#X: 1369 Y:  447 RGB: (204,   0,   0) ! left

#X:  635 Y:  701 RGB: (153, 141, 107) down right
#X:  635 Y:  541 RGB: (254, 236, 180) mid right
#X:  378 Y:  514 RGB: (255, 235, 182) up right
#X:  650 Y:  448 RGB: (204,   0,   0) ! right



while keyboard.is_pressed('q') == False:
    if pyautogui.pixelMatchesColor(1283,695,(253, 234,  183), tolerance=10) or pyautogui.pixelMatchesColor(635,701,(153, 141,  107), tolerance=10): #down
        time.sleep(0.2)
        pyautogui.press('w')
        print("down")
    elif pyautogui.pixelMatchesColor(1287,541,(254, 236,  181), tolerance=10) or pyautogui.pixelMatchesColor(635,541,(253, 236,  181), tolerance=10): #mid
        time.sleep(0.2)
        pyautogui.press('s')
        print("mid")
    elif pyautogui.pixelMatchesColor(1542,519,(253, 236,  180), tolerance=10): #up left
        time.sleep(0.1)
        pyautogui.press('a')
        print("up left")
    elif pyautogui.pixelMatchesColor(1369,447,(204, 0,  0), tolerance=10): #! left
        time.sleep(0.01)
        pyautogui.press('d')
        print("! left")
    elif pyautogui.pixelMatchesColor(378,514,(255, 235,  182), tolerance=10): #up right
        time.sleep(0.1)
        pyautogui.press('d')
        print("up right")
    elif pyautogui.pixelMatchesColor(650,448,(204, 0,  0), tolerance=10): #! right
        time.sleep(0.01)
        pyautogui.press('a')
        print("! right")
