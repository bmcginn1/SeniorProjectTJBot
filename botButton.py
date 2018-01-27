import RPi.GPIO as GPIO
from neopixel import *
import os
from time import sleep
import subprocess

LED_COUNT = 16
LED_PIN = 10
LED_FREQ_HZ = 800000
LED_DMA = 5
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0
LED_STRIP = ws.WS2811_STRIP_RGB
strip = Adafruit_NeoPixel(
            LED_COUNT,
            LED_PIN,
            LED_FREQ_HZ,
            LED_DMA,
            LED_INVERT,
            LED_BRIGHTNESS,
            LED_CHANNEL,
            LED_STRIP)
strip.begin()


GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

def startBot():
    os.system('sudo python3 /home/pi/tj-python-master/tjbot.py')
def restartProcess():
    os.system('sudo ./home/pi/tj-python-master/start.sh')

strip.setPixelColorRGB(0, 255, 255, 0)
strip.show()

thing = True
while thing == True:
    if GPIO.input(4)==True:
        sleep(.5)
        
        #startBot()
        strip.setPixelColorRGB(0, 255, 0, 255)
        strip.show()
        print("Starting")
        subprocess.Popen(["sudo", "python3", "/home/pi/tj-python-master/tjbot.py"])
        thing = False;
while True:
    #print("Bullshit")
    if GPIO.input(4)==True:
        strip.setPixelColorRGB(0, 255, 0, 0)
        strip.show()
        print("Stopping")
        sleep(.5)
        subprocess.Popen(["sudo" ,"/home/pi/tj-python-master/./start.sh"])
        #restartProcess()
        

GPIO.cleanup()


