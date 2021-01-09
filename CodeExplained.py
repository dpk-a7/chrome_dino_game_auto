# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 13:48:37 2021

@author: Deepak Avudiappan
"""
import pyautogui as pag 
from PIL import Image, ImageGrab 
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



def hit(key: 'keyboard button')->'presses the button':
    pag.keyDown(key)
    
def BG_detector(img: 'Grayscale image')-> 'detects background color at particular area':
    for m in range(100,300):
        for n in range(150,350):
            if img[m,n] > 127:
                return 'W'
            elif img[m,n] < 127:
                return 'B'

#For White Background
def detectorLW(img: 'Grayscale image')-> 'detects color at particular area':
    for i in range(400,550):
        for j in range(670,695):
            if img[i,j] >= 150:
                return True
    return False

def detectorUW(img: 'Grayscale image')-> 'detects color at particular area':
    for I in range(400,550):
        for J in range(560,620):
            if img[I,J] >= 150:
                return True
    return False

#For Black background
def detectorLB(img: 'Grayscale image')-> 'detects color at particular area':
    for i in range(400,550):
        for j in range(670,695):
            if img[i,j] < 150:
                return True
    return False

def detectorUB(img: 'Grayscale image')-> 'detects color at particular area':
    for I in range(400,550):
        for J in range(560,620):
            if img[I,J] < 150:
                return True
    return False
    
    
def mains():
    driver =  webdriver.Chrome(ChromeDriverManager().install())
    try:
        driver.maximize_window()
        driver.get('chrome://dino/')
    
    except Exception as e:
        pass
    time.sleep(3)
    pag.press('space')
    time.sleep(2)
    pag.press('up')
    while (1):
        image = ImageGrab.grab().convert('L')
        data = image.load()
        bg = BG_detector(data)
        if bg == 'B':
            if detectorLW(data) == True:
                hit('up')
            elif detectorUW(data) == True:
                hit('down')
                time.sleep(0.5)
                pag.keyUp('down')
        if bg == 'W':
            if detectorLB(data) == True:
                hit('up')
            elif detectorUB(data) == True:
                hit('down')
                time.sleep(0.5)
                pag.keyUp('down')
if __name__ == '__main__':  
    i = 4
    print('Starting in..5')
    time.sleep(1)
    while(i>0):
        print(f"-------------{i}")
        time.sleep(1)
        i-=1
    mains()
