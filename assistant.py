import os
import pyttsx3    #text to speech
import speech_recognition as  sr  # speech to text
import webbrowser
import datetime
import pyjokes
import time
def speech_text():
    while True:
        call_rec = sr.Recognizer()
        with sr.Microphone() as source:
                    print("Listining .....")
                    call_rec.adjust_for_ambient_noise(source)    #noise cancelation
                    audio = call_rec.listen(source)
                    try:
                        print("Recognizing ....")
                        data = call_rec.recognize_google(audio)
                        print(data)
                        return data
                    except sr.UnknownValueError:
                        print("Not understanding")
# text to speech
def text_speech(x):
    call_engine = pyttsx3.init()
    voices = call_engine.getProperty('voices')
    call_engine.setProperty('voice',voices[1].id)
    rate = call_engine.getProperty('rate')
    call_engine.setProperty('rate',125)
    call_engine.say(x)
    call_engine.runAndWait()

if __name__ == '__main__':
    if "mira" in speech_text().lower():
            text_speech("Hello how can i help you")
            while True:
                    data_1 = speech_text()
                    if "made" in data_1:
                        name = "The owner,my boss kaushik made me"
                        text_speech(name)
                    elif "old are you" in data_1:
                        age = "I don't know my age"
                        text_speech(age)
                    elif "home" in data_1:
                        home  = "My home is on Earth"
                        text_speech("home")
                    elif "time" in data_1:
                        time = datetime.datetime.now().strftime("%I%M%p")
                        text_speech(time)
                    elif "YouTube" in data_1:
                        result = "opening youtube "
                        text_speech(result)
                        webbrowser.open("https://www.youtube.com/")
                        break
                    elif "Google" in data_1:
                        result = "opening google"
                        text_speech(result)
                        webbrowser.open("https://www.google.co.in/")
                        break
                    elif "jokes" in data_1:
                        joke_1 = pyjokes.get_joke(language="en",category="neutral")
                        print(joke_1)
                        text_speech(joke_1)
                    elif "exit" in data_1:
                        text_speech("Exiting now Thank you have a good day")
                        break
                    elif "music" in data_1:
                        text_speech("opening spotify ")
                        os.system("spotify free")
                        break
                    else:
                        text_speech("sorry i didn't get")
    else:
        text_speech("Sorry , I can only activate if you call my real name.")