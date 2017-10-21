import pyautogui as pag
import sounddevice as sd
from time import sleep
import sys
duration = 1000*10  # seconds

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata
    if(indata[-1][0]>0.05):
    	pag.click()
    	sleep(0.03)
    	print(indata[-1])

with sd.Stream(channels=2, callback=callback):
    sd.sleep(int(duration * 1000))