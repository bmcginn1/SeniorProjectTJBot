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


Author: Brian McGinnis
Date: June 16 2017
Rev: 1.1
"""

from watson_developer_cloud import TextToSpeechV1
import json
import wave
import pyaudio
import os.path
from os.path import join, dirname
import subprocess


class TextToSpeech:

    def __init__(self, username, password):
        self.user = username
        self.pas = password
        self.text_to_speech = TextToSpeechV1(
            username=username,
            password=password,
            x_watson_learning_opt_out=True)
        self.fileLocation = "/home/pi/tj-python-master/resources/output.wav"


#beautiful Block of code
    def speak(self, message):
        print(message)
        if(message == "Welcome to CBU! We have a beautiful 75-acre campus and are the oldest degree granting university in Memphis. What else would you like to know about CBU?"):
            self.play("VisitorsResponse1")
        
        elif(message == "Welcome to Christian Brothers University! We are the oldest degree granting university in Memphis. We have a beautiful 75-acre campus! What else can I tell you about CBU?"):
            self.play("VisitorsResponse2")
        
        elif(message == '<speak><express-as type="GoodNews">Engineers, on your mark, get set, CALCULATE!</express-as><break strength="strong"></break> The 2017 Best Value Schools Top Small Colleges ranked our Chemical Engineering as number 1, Civil Engineering as number 3, Electrical Engineering at number 4, and Mechanical Engineering at number 4 in the nation. The 2017 U.S. News & World Report ranked CBU to have the Best Undergraduate Engineering program of the regional universities in the south. The School of Engineering also proudly holds a 96% Engineering Job Placement rate.</speak>'):
            self.play("TellMe1")
        
        elif(message == "<speak>Did you see that new building, Rosa Deal? It is very pretty and so is the art inside it. It houses great programs such as Art Therapy, Psychology, English, and undergraduate and masters education programs. It also has a state of the art, brand new Psychology lab. Bestvalueschools.com has ranked The Rosa Deal School of Arts degrees in English and Psychology #2 in best value for small colleges nationwide in 2016-2017. Both programs offer numerous paths of study including English, Creative Writing, English for Corporate Communications, Speech Pathology, and Cognitive Psychology. </speak>"):
            self.play("TellMe2") 
        
        elif(message == "<speak> Doctor, doctor, give me the news; I’ve got a bad case of wanting to study!  Besides a wide variety of areas of study, the School of Sciences has EXCELLENT placement rates into post-graduate or specialized schools of study: 94% for Nursing School, 93% for Pharmacy School, 89% for Physical Therapy School, 85% for Medical School, & 80 % for Physician Assistant Programs. </speak>"):
            self.play("TellMe3")
        
        elif(message == '<speak> Let me give you the Business!<break strength="strong"></break>  The School of Business offers a variety of concentrations in areas such as marketing, management, information systems, accounting, finance, banking, and International Business. We even have an interdisciplinary concentration that allows you to connect business concentrations with concentrations from other schools of study. You can even pursue your MBA in the same place post-graduation. </speak>'):
            self.play("TellMe4")
        
        elif(message == '<speak>What do you a call a Catholic service that is very important? <break strength="strong"></break><break strength="strong"></break> A Critical Mass</speak>'):
            self.play("joke1")
        
        elif(message == '<speak>How much did the pirate pay for his piercings? <break strength="strong"></break><break strength="strong"></break>  A buck-an-ear. </speak>'):
            self.play("joke2")
        
        elif(message == '<speak>What do you call a pirate with two eyes and two legs? <break strength="strong"></break><break strength="strong"></break> A rookie. </speak>'):
            self.play("joke3")
        
        elif(message == "<speak>Do you want to know about athletics or finances? </speak>"):
            self.play("TellMeBucs")
        
        elif(message == "<speak>97% of our students receive financial assistance. Make sure you participate in one of our scholarship competitions. </speak>"):
            self.play("money")
        
        elif(message == "<speak>CBU participates in NCAA Division II sports. CBU has 15 intercollegiate teams in the Gulf South Conference. </speak>"):
            self.play("athletics")
        
        elif(message == "Cody Black and Brian McGinnis created me. Their legacy will live long at CBU."):
            self.play("creator1")
        
        elif(message == "I was birthed from the black hole of the school of engineering. That's all that I know."):
            self.play("creator2")
        
        elif(message == "My name is Bonnie. I am named after the famous Caribbean buccaneer, Anne Bonnie. You should google her! By the way, do you like my eyepatch?"):
            self.play("name")
        
        elif(message == "<speak>Painting the Rock is my favorite tradition. Students paint messages varying from birthday messages to club announcements. I even had a friend be proposed to on the rock. </speak>"):
            self.play("inquiry1")
        
        elif(message == "<speak>Lasallian Education centers on Catholic values and personal relationships, emphasizing academic excellence, faith formation, inclusion, respect for the individual, service and social justice. A Lasallian Education strives to enrich each student’s cultural, intellectual, physical, social and spiritual development. </speak>"):
            self.play("inquiry2")
        
        elif(message == "<speak>CBU has a very active Greek community. We have Pan Hallenic, IFC, and NPHC fraternities and sororities. Their philanthropies include autism awareness, military heroes, breast cancer awareness, St. Jude, and many others. </speak>"):
            self.play("inquiry3")
        
        elif(message == "I love Central Barbecue! Did you know it is within walking distance of campus?"):
            self.play("inquiry4")
        
        elif(message == "September 19th! National talk like a pirate day!"):
            self.play("inquiry5")
        
        elif(message == "97% of CBU graduates have jobs or are in graduate school within one year of graduation. CBU guarantees internships to all students, which is a great way to make connections that can lead to jobs after graduation."):
            self.play("inquiry6")
        
        elif(message == "Sorry, what would you like to know about?"):
            self.play("inquiry7")
                      
        elif(message == "I didn't understand. You can try rephrasing."):
            self.play("saywhat")
        
        elif(message == "Can you reword your statement? I'm not understanding."):
            self.play("saywhat1")
                      
        elif(message == "I didn't get your meaning."):
            self.play("saywhat2")
        
        else: #not a saved response so it just does this
            with open(join(dirname(__file__), self.fileLocation), 'wb') as audio_file:
                    audio_file.write(
                        self.text_to_speech.synthesize(
                            message,
                            accept='audio/wav',
                            voice="en-US_AllisonVoice"))

            subprocess.call("exec aplay " + self.fileLocation, shell=True)
    
    def play(self, filename):
        responsePath = "/home/pi/tj-python-master/resources/" + filename + ".wav"
        subprocess.call("exec aplay " + responsePath, shell=True)

        # old code going to run it with system calls
        # define stream chunk
        # chunk = 4096
        # open a wav forat music
        # f = wave.open(r"resources/output.wav","rb")
        # instantiate PyAudio
        # p = pyaudio.PyAudio()
        # open stream
        # stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
        # channels = f.getnchannels(), rate = f.getframerate(), output = True)
        # read data
        # data = f.readframes(chunk)
        # play stream
        # while data:
        #         stream.write(data)
        #         data = f.readframes(chunk)
        # stop stream
        # stream.stop_stream()
        # stream.close()
        # close PyAudio
        # p.terminate()

# tts = TextToSpeech('2cb70eda-ccc5-40d7-adee-91c9aa249841', 'zyzBtEqo73D7')
# tts.speak('I believe I know what you are saying')
