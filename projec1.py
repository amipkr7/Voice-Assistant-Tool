import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os

def speechtx(x):
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	engine.setProperty('voice',voices[1].id)
	rate = engine.getProperty('rate')
	engine.setProperty('rate',120)
	engine.say(x)
	engine.runAndWait()

def sptext():
    recognizer = sr.Recognizer()  
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")  
            data = recognizer.recognize_google(audio)
            print(data)
            speechtx(data)
            return data
            
        except sr.UnknownValueError:
            print("Not Understood") 


sptext()


if __name__ == '__main__':
    data1 = sptext().lower()
    # while "bye" in data1:
    if "your name" in data1:
        name = "my name is Alexa"
        speechtx(name)
    elif "old are you" in data1:
        age = "i am 1 years old"
        speechtx(age)
    elif 'time' in data1:
    	time=datetime.datetime.now().strftime("%I%M%p")
    	speechtx(time)
    elif 'youtube' in data1:
    	webbrowser.open("https://www.youtube.com/")
    elif 'joke' in data1:
    	joke1=pyjokes.get_joke(language="en",category="neutral")
    	speechtx(joke1)