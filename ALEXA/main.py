import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import requests


engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    speak("Hello Sir ...I'm Mihir Assistant , How can I help you boss ? ")

def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening..")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognising...")
            query = r.recognize_amazon(audio, language='en-in')
            print(f"user said:  {query}\n")

        except Exception as e:
            print("Say that again please...")
            return "None"
        return query


    
if __name__ =='__main__':
    wishMe()
         #if 1:
    query = takeCommand().lower()

        #Logic for executing tasks based on query
    if 'wikipedia' in query:
        speak("searching wikipedia")
        query = query.replace('wikipedia', "")
        results = wikipedia.summary(query, sentences=2)
        speak("according to wikipedia") 
        print(results)
        speak(results)


    elif 'open youtube' in query:
        webbrowser.open("youtube.com")


    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'who creates you' in query:
        speak("Mihir created me")


    elif ' how are you' in query:
        speak("I am fine")

    elif 'logout' in query:
        speak("Thank you")
        exit()
         

        