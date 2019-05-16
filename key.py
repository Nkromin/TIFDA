import speech_recognition as sr
import cv2
import os

import pyautogui as pag
import time

from pykeyboard import PyKeyboard


def talkToMe(audio):
    "speaks audio passed as argument"

    # print(audio)

    for line in audio.splitlines():
        os.system("say " + audio)

    #  use the system's inbuilt say command instead of mpg123

    #  text_to_speech = gTTS(text=audio, lang='en')

    #  text_to_speech.save('audio.mp3')

    #  os.system('mpg123 audio.mp3')


def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    keyb = PyKeyboard()

    with sr.Microphone() as source:

        print('Ready...')

        r.pause_threshold = 0.5

        r.adjust_for_ambient_noise(source, duration=1)

        audio = r.listen(source)

    try:

        command = r.recognize_google(audio).lower()

        print('You said: ' + command + '\n')
        if (command == 'right click'):
            pag.click(button='right')
        elif (command == 'left click'):
            pag.click(button='left')
        elif (command == 'double right click'):
            pag.click(button='right', clicks=2)
        elif (command == 'double left click'):
            pag.click(button='left', clicks=2)
        elif (command == '\n'):
            pag.press('enter')
        elif (command == 'dot'):
            pag.press('.')
        elif (command == 'backspace' or command == 'delete'):
            pag.press('backspace')
        elif (command == 'select all'):
            pag.hotkey('ctrl', 'a')
        elif (command == 'plus one'):
            pag.hotkey('ctrl', '+')
        elif (command == '-1'):
            pag.hotkey('ctrl', '-')
        elif (command == 'exit'):
            os._exit()
        else:
            pag.click(button='left', clicks=2)
            keyb.type_string(command)



    # loop back to continue to listen for commands if unrecognizable speech is received

    except sr.UnknownValueError:

        print('Your last command couldn\'t be heard')

        command = myCommand();

    return command


'''

def note():
    while True:
        comm=myCommand();
        keyboard.write(comm)
        if (comm=='ok'):
            break

'''


def assistant(command):
    "if statements for executing commands"


'''

    if 'notepad' in command:
        app=application.Application()

        note()

    elif 'web browser' in command:
        app1=application.Application()
        app1.start("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        web()

    else:

            talkToMe('I don\'t know what you mean!')

'''

talkToMe('I am ready for your command')

# loop to continue executing multiple commands

while True:
    assistant(myCommand())





