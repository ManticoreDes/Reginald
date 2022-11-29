
from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import configparser
from datetime import datetime  # isort: skip
import os  # isort: skip
import smtplib  # isort: skip
import gui  # isort: skip
import speech_recognition as sr  # isort: skip
import subprocess
import wolframalpha
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # hides terminal message on boot

from actions import (  # isort: skip
    change_rate,
    change_voice,
    change_volume,
    search_engine_selector,
    set_gui_speak,
    speak,
    wish_me,
)

from commands import (  # isort: skip
    command_bye,
    command_hello,
    command_nothing,
    command_open,
    command_play_music,
    command_search,
    command_whatsup,
    command_wife,
    command_wikipedia,
    command_date,
    command_launch,
    # command_exit,
)

popular_websites = {
    "salesforce": "https://mc.login.exacttarget.com/hub-cas/login",
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "wikipedia": "https://www.wikipedia.org",
    "amazon": "https://www.amazon.com",
    "github": "https://www.github.com",
    "netflix": "https://www.netflix.com/browse",
    "gmail": "https://mail.google.com/mail/u/0/#inbox",
    "huntington": "https://www.huntington.com",
    "calendar": "https://calendar.google.com/",
}

def main(search_engine, take_command, debug):
    def execute_the_command_said_by_user():
        query = take_command()

        # executing commands without arguments
        phrases = {
            "what's up": command_whatsup,
            "what's todays date": command_date,
            "abort": command_nothing,
            "stop": command_nothing,
            "hello": command_hello,
            "goodbye": command_bye,
            "bye": command_bye,
            "shutdown": command_bye,
            "load up league": command_launch,

            # "exit game": command_exit,
            "play music": command_play_music,
        }
        for phrase, command in phrases.items():
            if phrase in query:
                command()

# BASIC COMMANDS -->

        if "Wikipedia" in query:
            command_wikipedia(debug, query)

        elif "open" in query:
            command_open(
                query,
                popular_websites,
                debug,
                search_engine,
                take_command
            )

        elif "search" in query:
            command_search(query, search_engine)

        elif "date" in query or "day is" in query:
            speak(f"{datetime.now():%A, %B %d, %Y}")

        elif "time" in query:
            speak(f"{datetime.now():%I %M %p}")

        elif "change rate" in query:
            change_rate(query, take_command)

        elif "change voice" in query.lower():
            change_voice(query, take_command)

        elif "change volume" in query.lower():
            change_volume(query, take_command)

# ADVANCED COMMANDS -->

        elif "calculate" in query:
            try:
                app_id = "W8HHEE-6AY35T3RYV"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)
            except Exception as e:
                speak("please repeat that calculation sir")

        elif "League of Legends" in query or "League" in query:
            subprocess.call(["C:\Riot Games\League of Legends\LeagueClient.exe"])

        elif "Notepad" in query:
            subprocess.call(["C:\Program Files\Windows NT\Accessories\wordpad.exe"])

# CONVERSATION -->

        elif "Good Morning" in query or "Good Afternoon" in query or "what up" in query or "how are you" in query or "how's it" in query:
            command_whatsup()

        elif "test" in query or "Isis" in query or "wife" in query or "better half" in query or "love of my life" in query or "icey" in query:
            command_wife()

    gui.set_speak_command(execute_the_command_said_by_user)
    set_gui_speak(gui.speak)
    gui.mainloop()


# RUN

def run():
    master = config['DEFAULT']['master']

    search_engine = search_engine_selector(config)

    debug = config['DEFAULT']['debug']

    if debug == "True":
        def take_command():
            return input("Command |--> ")
    else:
        def take_command():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening....")
                r.pause_threshold = 0.5
                r.energy_threshold = int(config['DEFAULT']['energy_threshold'])
                audio = r.listen(source)

            query = " "
            try:
                print("Recognizing....")
                query = r.recognize_google(audio, language="en-in")
                print("user said: " + query)

            except sr.UnknownValueError:
                if debug == "True":
                    print("Sorry Could You please try again")
                else:
                    pass
                speak("Sorry Could You please try again")

            except Exception as e:
                if debug == "True":
                    print(e)
                    print("Say That Again Please")
                else:
                    pass

            return query

    speak(text="Initializing Reginald....")
    wish_me(master)
    main(search_engine, take_command, debug)

if os.path.isfile('./config.ini'):  # Checks if config.ini exists.
    config = configparser.ConfigParser()  # if exists loads library.
    config.read('config.ini')  # and also the file.
    run()  # Then it launches the main program
else:
    # if it doesn't exist it drops an error message and exits.
    print('You need a config.ini file.')
    print('Check the documentation in the Github Repository.')

# CALANDER -->


def authenticate_google():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json')
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    return service


def get_events(n, service):
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print(f'Getting the upcoming {n} events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=n, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])


service = authenticate_google()
get_events(2, service)