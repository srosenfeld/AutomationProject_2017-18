#We always put our "import" modules at the top of the program
import pyautogui as pg
import time
import webbrowser

#Here is our newest "import" module - just like "pg" is the abbreviation for pyautogui, "wincl" is the abbreviation for win32com.client
import win32com.client as wincl

# we create a variable called "speak" which will make it even easier to call the "Speak" function
speak = wincl.Dispatch("SAPI.SpVoice")


#Now let's make our PC talk!
#Use the function speak.Speak() to make it read your text out loud
speak.Speak("Hello world!")

speak.Speak("This is the PC voice speaking.")

speak.Speak("How are you doing today?")

answer = pg.prompt("How are you doing today?")

if answer == "Good":
    speak.Speak("That's wonderful.")
