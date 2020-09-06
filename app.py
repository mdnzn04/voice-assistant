import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from random import randint

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Ada. Sir How may i help you")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="eng-in")
        print(f"user said:{query}\n")
    except Exception:
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia"," ")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            speak(results)
        elif "open youtube" in query:
            webbrowser.open('youtube.com')

        elif "open google" in query:
            webbrowser.open('google.com')

        elif "play music" in query:
            music="D:\\nzn\\music"
            songs = os.listdir(music)
            for _ in range(100):
                value = randint(0, 100)
            os.startfile(os.path.join(music,songs[value]))

        elif "the time" in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)

        elif "open chrome" in query:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

