import pyttsx3
import speech_recognition as sr
import random
import os
import sys
from acce import *
from time import sleep
import os.path

global engine
engine = pyttsx3.init()
engine.setProperty('rate',140)
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')

global r
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything\n")
    audio = r.listen(source, phrase_time_limit=1)
    try:
        text = r.recognize_google(audio)
        formated = format(text)
        print(formated)
        if formated == 'hello' or formated == 'hey' or formated == 'hi':
            engine.say(random.choice(greetings))
            engine.runAndWait()
            while True:
                try:
                     print("How may I help you? ")
                     text = r.recognize_google(audio)
                     formated = format(text)
                     print(formated)
                     if formated == 'do you have a name' or formated == 'what is your name' or formated == 'do you have a name':
                         engine.say(random.choice(names))
                         engine.runAndWait()

                     elif formated == 'who is your God' or formated == 'who made you' or formated == 'who invented you':
                         engine.say(random.choice(developer))
                         engine.runAndWait()

                     elif formated == 'who is your developer' or formated == 'who developed you':
                         engine.say("My developer's name is Ajay, he developed me")
                         engine.runAndWait()
                     elif formated == 'shutdown the pc' or formated == 'shutdown' or formated == 'close':
                          engine.say(random.choice(s))
                          engine.runAndWait()
                          sleep(2)
                          os.system("shutdown /s /t 1")

                     elif formated == 'restart the pc' or formated == 'restart':
                          engine.say(random.choice(r))
                          engine.runAndWait()
                          sleep(2)
                          os.system("shutdown /r /t 1")

                     elif formated == 'create a file':
                        engine.say("What do you want to name the file?")
                        engine.runAndWait()
                        f_name = r.listen(source, phrase_time_limit=3)
                        name = r.recognize_google(f_name)
                        file_name = format(name)
                        f = open(file_name,'x')
                        if os.path.exists(file_name) is True:
                            engine.say("File "+file_name+" Created")
                            engine.runAndWait()

                except:
                    engine.say(random.choice(error))
                    engine.runAndWait()
                    print("")
        else:
            print("")
    except:
        print("")

