import pyautogui as pag
import sounddevice as sd
from time import sleep
import sys
duration = 1000*10  # seconds

loudness = 0.01 #adjust how loud you have to be to shoot.

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata
    if(indata[-1][0]>loudness):
    	pag.click()
    	sleep(0.1)
    	print(indata[-1])

with sd.Stream(channels=2, callback=callback):
    sd.sleep(int(duration * 1000))