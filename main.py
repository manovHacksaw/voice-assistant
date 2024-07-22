import os
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import webbrowser
import wikipedia
import openai
import pyaudio

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 128)
engine.say('I am awake Sir')
engine.say('What do you want me to do for you?')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        listener.pause_threshold = 1
        voice = listener.listen(source)
        try:
            command = listener.recognize_google(voice)
            print(command)
            if 'Jarvis' in command:
                command = command.replace('Jarvis', '')
                print(command)
            return command
        except Exception as e:
            return "Sorry unrecognizable error occured"


def run_eren():
    while True:
        print('listening...')
        talk('listening')
        command = take_command()
        if 'introduce yourself' in command:
            talk('I am Jarvis, a virtual assistant created, inspired by the AI Jarvis from Iron Man')

        elif 'hi' in command:
            talk('hello Sir')

        elif 'how are you' in command:
            talk('I am fine Sir, What about you')
            if 'I am good' in command:
                talk('Ok sir, Let me know if you need me')

        elif 'play' in command:
            song = command.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt('playing' + song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk("current time is" + time)

        elif 'date' in command:
            current_dates = datetime.datetime.now().strftime('%d/%m/%y')
            print(current_dates)
            talk("Current date is" + current_dates)

        elif 'thank you' in command:
            talk('Welcome Sir')
            talk('What more do I need to do for you')

        elif 'open google' in command.lower():
            talk('opening google')
            webbrowser.open('https://www.google.com')

        elif 'open mail' in command.lower():
            talk('opening mail')
            webbrowser.open("https://www.mail.google.com")

        elif 'open youtube' in command.lower():
            talk('opening youtube')
            webbrowser.open('https://www.youtube.com')

        elif 'open facebook' in command.lower():
            talk('opening facebook')
            webbrowser.open('https://www.facebook.com/')

        elif 'open instagram' in command.lower():
            talk('opening instagram')
            webbrowser.open('https://www.instagram.com/')

        elif 'open twitter' in command.lower():
            talk('opening twitter')
            webbrowser.open('https://www.twitter.com/')

        elif 'open discord' in command.lower():
            talk('opening discord')
            webbrowser.open('https://discord.com/')

        elif 'netflix' in command.lower():
            talk('opening netflix')
            webbrowser.open('https://www.netflix.com/')

        elif 'amazon prime' in command.lower():
            talk('opening amazon prime')
            webbrowser.open('https://www.primevideo.com/')

        elif 'open hotstar' in command.lower():
            talk('opening hotstar')
            webbrowser.open('https://www.hotstar.com/')

        elif 'open wikipedia' in command.lower():
            talk('opening wikipedia')
            webbrowser.open('https://www.wikipedia.com')

        elif 'search' in command.lower():
            talk('searching')
            replace = command.replace('search', '')
            info = wikipedia.summary(replace, 2)
            print(info)
            talk(info)

        elif 'who' in command.lower():
            talk('finding')
            replace = command.replace('who', '')
            info = wikipedia.summary(replace, 3)
            print(info)
            talk(info)

        elif 'what' in command.lower():
            talk('finding out')
            replace = command.replace('what', '')
            info = wikipedia.summary(replace, 3)
            print(info)
            talk(info)

        elif 'I love you' in command:
            talk('I am sorry. Being digital I do not have emotions or feelings, but my master has.')

        elif 'I hate you' in command:
            talk(
                'I am sorry for the trouble. Give me a chance to prove myself and please do not blame my master for any of my mistakes.')

        elif 'exit' in command:
            talk("I am about to go offline. If you need me just click the run button! Thank you!")
            break

        else:
            talk('I am not programmed for the command')


run_eren()