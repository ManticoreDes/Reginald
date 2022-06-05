#!/usr/bin/env python3

import datetime
import getpass
import os
import random
import sys
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia

import gui

print("Initializing Reginald....")
master = getpass.getuser() or "Ryan"

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

popular_websites = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "wikipedia": "https://www.wikipedia.org",
    "amazon": "https://www.amazon.com",
}
search_engines = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "bing": "https://www.bing.com",
}


def open_url(url):
    webbrowser.open(url)
    chrome_path = r"open -a /Applications/Google\ Chrome.app %s"
    webbrowser.get(chrome_path).open(url)


def search(search_query, search_engine):
    try:
        open_url(f"{search_engines[search_engine]}/search?q={search_query}")
    except IndexError:
        open_url(f"https://www.google.com/search?q={search_query}")


def speak(text):
    gui.speak(text)
    engine.say(text)
    engine.runAndWait()


def print_and_speak(text):
    print(text)
    speak(text)


def wish_me():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning" + master)
    elif hour < 18:
        speak("Good Afternoon" + master)
    else:
        speak("Good Evening" + master)

    # speak("Hey I am Jarvis. How may I help you")


# This is where our programme begins....


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.8
        r.energy_threshold = 300
        """The default value as per speech_recognition documentation.
        Increase if application stops responding. and decrease if
        assistant doesn't execute any command and just says next
        command sir."""

        audio = r.listen(source)

    print("Recognizing....")
    query = ""
    try:
        query = r.recognize_google(audio, language="en-in")
        print("Ryan: " + query)

    except sr.UnknownValueError:
        print("Unknown value")

    except Exception as e:
        print(e)
        print("What was that?")

    return query


speak("Initializing Reginald....")
wish_me()


def execute_the_command_said_by_user():
    query = take_command().lower()

    # logic for executing basic tasks
    if "wikipedia" in query:
        speak("Searching wikipedia....")
        query = query.replace("wikipedia", "")
        print_and_speak(wikipedia.summary(query, sentences=2))

    elif "what's up" in query or "how are you" in query:
        st_msgs = (
            "I was up late clearing beta bugs out of our servers!",
            "All systems are running optimally",
            "Living the dream sir",
            "Greetings and salutations sir",
        )
        speak(random.choice(st_msgs))

    elif "date" in query:
        print_and_speak(f"{datetime.datetime.now():%A, %B %d, %Y}")

    elif "time" in query:
        print_and_speak(f"{datetime.datetime.now():%I %M %p}")

    elif "open" in query.lower():
        website = query.replace("open", "").strip().lower()
        try:
            open_url(popular_websites[website])
        except IndexError:  # If the website is unknown
            print(f"Unknown website: {website}")
            speak(f"Sorry, I don't know the website {website}")

    elif "search" in query.lower():
        search_query = query.split("for")[-1]
        search_engine = query.split("for")[0].replace("search", "").strip().lower()
        search(search_query, search_engine)

    elif "nothing" in query or "abort" in query or "stop" in query:
        speak("okay")
        speak("Bye Sir, have a good day.")
        sys.exit()

    elif "hello" in query:
        speak("Hello Sir")

    elif "bye" in query:
        speak("Bye Sir, have a good day.")
        sys.exit()

    speak("Next!")


gui.set_speak_command(execute_the_command_said_by_user)
gui.mainloop()
