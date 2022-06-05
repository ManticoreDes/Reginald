import configparser
from multiprocessing.connection import wait
import random
import sys
import datetime
import wikipedia
import datetime
from pygame import mixer
from actions import open_url, search, speak

config = configparser.ConfigParser()  # if exists loads library.
config.read('config.ini')


def command_wikipedia(debug, query):
    speak("Searching wikipedia....")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    if debug == "True":
        print(results)
    else:
        pass
    speak(results)


def command_whatsup():
    st_msgs = [
        "I was up late clearing beta bugs out of our servers!",
        "All systems are running optimally",
        "Living the dream sir",
        "Greetings and salutations sir",
    ]
    speak(random.choice(st_msgs))


def command_open(query, popular_websites, debug, search_engine, take_command):
    website = query.replace("open", "").strip().lower()
    try:
        open_url(popular_websites[website])
    except KeyError:  # If the website is unknown
        if debug == "True":
            print(f"Unknown website: {website}")
        else:
            pass
        speak(f"add {website} to list please")
        speak(f"¿Shall I search {website} ?")
        if take_command() == "yes":
            search(website, search_engine)
        else:
            pass


def command_search(query, search_engine):
    search_query = query.split("for")[-1]
    search(search_query, search_engine)


def command_nothing():
    speak("okay")


def command_hello():
    speak("Hello Sir")


def command_bye():
    speak("Bye Sir, have a good day.")
    sys.exit()

def command_date():
    speak(f"{datetime.datetime.now():%A, %B %d, %Y}")

def command_play_music():
    open_url("https://www.youtube.com/watch?v=eg_V56BUmh0")






