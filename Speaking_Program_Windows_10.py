import win32com.client as wincl
import pyautogui as pg
import time
import webbrowser
speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("This is the PC voice speaking.")

speak.Speak("How are you doing today?")

answer = pg.prompt("How are you doing today?")

if answer == "Good":
    speak.Speak("That's wonderful.")
