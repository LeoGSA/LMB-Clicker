# -*- coding: utf-8 -*-
# © LeoGSA - Sergey Grigoriev (leogsa@gmail.com)

"""
This program allows to do many Left_Mouse_Button Clicks automatically.
1) You point a mouse
2) press Enter
Program does 50 Left_Mouse_Button Clicks at chosen point.
"""
import pyautogui
import ctypes
import time
import sys

pyautogui.FAILSAFE = True
hllDll = ctypes.WinDLL ("User32.dll")

def get_space_state():
    return hllDll.GetKeyState(0x20)

def get_enter_state():
    return hllDll.GetKeyState(0x0D)

def keyboard(clicks):
    while True:
        time.sleep(0.02)
        if get_space_state() < 0:
            print ("Space pressed")
            pyautogui.click(clicks=clicks, interval=0.01) # вот тут указываете кол-во кликов и интервал между ними в миллисекундах
        if get_enter_state() > 1:
            print ('Stopped.')
            break

if __name__ == '__main__':
    clicks = 50
    if len(sys.argv) > 1:
        clicks = int(sys.argv[1])
    print ('Started.\nSpace = '+str(clicks)+' clicks.'+'\nPress Enter to stop.')
    keyboard(clicks)







