from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

#(238, 238, 238) target
#(255, 255,   0) star
#(242, 244, 231) cloud

def click(x,y):
    win32api.SetCursorPos((x,y))
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    #win32api.SetCursorPos((x,y))




while keyboard.is_pressed('q') == False:
    flag = 0
    pic = pyautogui.screenshot(region=(335 , 0 , 1080 , 1080 ))
    width, height = pic.size

    for x in range(0, width, 2):
        for y in range(0, height, 2):


            r, g, b = pic.getpixel((x, y))

            if b == 238 and r == 238 and g == 238: #target
                flag = 1
                click(x+355, y+15)
                break
            
            elif b == 0 and r == 255 and g == 255: #star
                flag = 1
                click(x+335, y+10)
                break

            elif b == 231 and r == 242 and g == 244: #cloud
                flag = 1
                click(x+350, y+10)
                break

        if flag == 1:
            break
