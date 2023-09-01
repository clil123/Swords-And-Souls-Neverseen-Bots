from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

target = (238, 238, 238)
man = (193, 180, 160)
coin = (255, 225, 100)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)



while keyboard.is_pressed('q') == False:
    flag = 0
    pic = pyautogui.screenshot(region=(335 , 0 , 1080 , 1080 ))
    width, height = pic.size

    for x in range(0, width, 10):
        for y in range(0, height, 10):


            r, g, b = pic.getpixel((x, y))

            
            if r == target[0] and g > 130 and b > 130 : #target
                print("target")
                flag = 1
                print("time before target = ", time.perf_counter(), "location = ", x,y)
                click(x+355, y+15)
                print("time after target = ", time.perf_counter(), "location = ", x,y)
                time.sleep(0.05)
                break
            
            elif b == man[2] and r == man[0] and g == man[1]: #man
                print("man")
                flag = 1
                print("time before man = ", time.perf_counter())
                click(x+350, y+10)
                print("time after man = ", time.perf_counter())
                time.sleep(0.05)
                break

            elif b == coin[2] and r == coin[0] and g == coin[1]: #coin
                print("coin")
                flag = 1
                print("time before coin = ", time.perf_counter())
                click(x+335, y)
                print("time after coin = ", time.perf_counter())
                time.sleep(0.05)
                break

        if flag == 1:
            break
