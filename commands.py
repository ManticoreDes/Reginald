import configparser
from multiprocessing.connection import wait
import random
import sys
import datetime
import wikipedia
import datetime
import subprocess

from pygame import mixer
from actions import open_url, search, speak

config = configparser.ConfigParser()  # if exists loads library.
config.read('config.ini')

# CONVERSATION -->

def command_whatsup():
    st_msgs = [
        "I was up late clearing beta bugs out of our servers!",
        "All systems are running optimally",
        "Living the dream sir",
        "Greetings and salutations sir",
    ]
    speak(random.choice(st_msgs))

def command_hello():
    st_msgs = [
        "didnt see you there, please do call upon me if you deem it necessary",
        "Hello to you as well",
        "Greetings and salutations sir",
    ]
    speak(random.choice(st_msgs))

def command_bye():
    st_msgs = [
        "Transitioning to sleep state sir",
        "Entering sleep cycle",
        "Powering down Sir",
    ]
    speak(random.choice(st_msgs))
    sys.exit()

def command_wife():
    st_msgs = [
        "good to see you again m'lady, you are radiant as ever",
        "Hello m'lady ",
        "Finally a breath of elegance in this dusty hovel",
    ]
    speak(random.choice(st_msgs))

def command_nothing():
    speak("okay")

def command_date():
    speak(f"{datetime.datetime.now():%A, %B %d, %Y}")


# SEARCH -->

def command_wikipedia(debug, query):
    speak("Searching Wikipedia....")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    if debug == "True":
        print(results)
    else:
        pass
    speak(results)

def command_search(query, search_engine):
    search_query = query.split("for")[-1]
    search(search_query, search_engine)


# OPEN CHROME TAB FROM popular_websites LIST IN Reginald.py -->

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


# LAUNCH APPLICATIONS -->

def command_launch():
    subprocess.call(["C:\Riot Games\League of Legends\LeagueClient.exe"])

# COMMAND -->

def command_play_music():
    open_url("https://www.youtube.com/watch?v=dQw4w9WgXcQ")






