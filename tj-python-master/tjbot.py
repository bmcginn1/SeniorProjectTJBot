#!/usr/bin/env python

"""

                  888
                  888
                  888
88888b.   .d88b.  88888b.   .d88b.  888  888
888 "88b d88""88b 888 "88b d88""88b `Y8bd8P'
888  888 888  888 888  888 888  888   X88K
888  888 Y88..88P 888 d88P Y88..88P .d8""8b.     http://nobox.io
888  888  "Y88P"  88888P"   "Y88P"  888  888     http://github.com/noboxio


TJBot

Author: Brian McGinnis
Date: 6/23/17
"""

import conversation
import ledProcess
import led
import servoProcess
import servo
import musicProcess
import music
import textToSpeech
import streaming
import time
import RPi.GPIO as GPIO




def main():

    try:
        stt = streaming.StreamingSTT(

            # replace with speech to text credentials username
            '1f900d96-d3fa-40f0-ab53-9a600f931796',

            # replace with speech to text credentials password
            'GAyuVqI1EEMv')
    except:
        fatalFailure()
    try:
        tts = textToSpeech.TextToSpeech(

            # replace with text to speech credentials username
            '2cb70eda-ccc5-40d7-adee-91c9aa249841',

            # replace with text to speech credentials password
            'zyzBtEqo73D7')
    except:
        fatalFailure()

    try:
        convo = conversation.Conversation(

            # replace with conversation credentials username
            '154b5b29-d1ca-4ff2-be09-c33c5e1d9e20',

            # replace with conversation credentials password
            'pmNftYlpvMS8',

            # replace with workspace ID.
            'da21184b-ae02-4159-9727-d994fc1bbaaf')
    except:
        fatalFailure()
    # replace with robot name
    name = 'Bonnie'

    servo_obj = servo.Servo()
    servoP = servoProcess.ServoProcess(servo_obj)
    led_obj = led.Led()
    ledP = ledProcess.LedProcess(led_obj)

    music_obj = music.Music("/home/pi/tj-python/resources/music.wav")
    musicP = musicProcess.MusicProcess(music_obj)

    time.sleep(.5)
    ledP.red()
    time.sleep(.5)
    ledP.green()
    time.sleep(.5)
    ledP.blue()
    time.sleep(.5)

    ledP.rainbowCycle(.0001, 99999999999999)

    # tts.speak("Hello, just a moment while I boot up")
    servoP.wave(3)

    """l = led.Led()
    le = ledProcess.LedProcess(l)
    print('sleeping')
    time.sleep(3)
    print('done sleeping, Lets Strobe')
    le.strobe()
    #le.customColor(255,0,0)
    print('sleeping')
    time.sleep(3)
    print('kill in 2')
    time.sleep(2)
    le.customColor(255,0,0)
    #le.stop()
    print('dead') """

    tts.speak('Hello my name is ' + name + ' I am the CBU admissions bot')






    while True:
        ledP.blue()
        try:
            phrase = stt.get_phrase()
        except:
            ledP.red()
        ledP.orange()
        if (name in phrase) or ('bunny'in phrase) or ('body' in phrase) or ('Bani' in phrase):
            response = convo.sendMessage(phrase)
            ledP.green()
            #response = response.upper()
            if '~' in response:
                print('Command Found')
                if '~RED' in response:
                    ledP.red()
                    response = response.replace('~RED', '', 1)
                if '~ORANGE' in response:
                    ledP.orange()
                    response = response.replace('~ORANGE', '', 1)
                if '~YELLOW' in response:
                    ledP.yellow()
                    response = response.replace('~YELLOW', '', 1)
                if '~GREEN' in response:
                    ledP.green()
                    response = response.replace('~GREEN', '', 1)
                if '~BLUE' in response:
                    print('Its Blue')
                    ledP.blue()
                    response = response.replace('~BLUE', '', 1)
                if '~PURPLE' in response:
                    ledP.purple()
                    response = response.replace('~PURPLE', '', 1)
                if '~PINK' in response:
                    ledP.pink()
                    response = response.replace('~PINK', '', 1)
                if '~WHITE' in response:
                    ledP.white()
                    response = response.replace('~WHITE', '', 1)
                if '~RAINBOW' in response:
                    ledP.rainbow()
                    response = response.replace('~RAINBOW', '', 1)
                if '~RAINBOWCYCLE' in response:
                    ledP.rainbowCycle()
                    response = response.replace('~RAINBOWCYCLE', '', 1)
                if '~MUSICPLAY' in response:
                    musicP.play()
                    response = response.replace('~MUSICPLAY', '', 1)
                if '~MUSICSTOP' in response:
                    musicP.stop()
                    response = response.replace('~MUSICSTOP', '', 1)
                if '~LEDOFF' in response:
                    ledP.off()
                    response = response.replace('~LEDOFF', '', 1)
                if '~ARMSTOP' in response:
                    servoP.stop()
                    response = response.replace('~ARMSTOP', '', 1)
                if '~ARMUP' in response:
                    servoP.armUp()
                    response = response.replace('~ARMUP', '', 1)
                if '~ARMDOWN' in response:
                    servoP.armDown()
                    response = response.replace('~ARMDOWN', '', 1)
                if '~DANCE' in response:
                    servoP.wave(10)
                    ledP.rainbowCycle(1, 50)
                    response = response.replace('~DANCE', '', 1)
                if '~ARMANGLE' in response:
                    response = response.replace('~ARMANGLE', '', 1)
                    param = int(response.split("~", 1)[0])
                    response = response.split("~", 1)[1]
                    servoP.angle(param)
                if '~ARMWAVECOUNT' in response:
                    response = response.replace('~ARMWAVECOUNTARMANGLE', '', 1)
                    param = int(response.split("~", 1)[0])
                    response = response.split("~", 1)[1]
                    servoP.wave(param)
                if '~ARMWAVE' in response:
                    servoP.wave(2)
                    response = response.replace('~ARMWAVE', '', 1)
                if response == '':
                    response = 'awkward silence'
            ledP.pink()
            tts.speak(response)

def fatalFailure():
    while(True):
        ledP.red()
        time.sleep(500)
        ledP.customColor(0,0,0)
        time.sleep(500)


if __name__ == "__main__":
    main()
