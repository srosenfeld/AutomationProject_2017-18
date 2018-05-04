#!/usr/bin/env python3
#This source code comes from the project: https://github.com/Uberi/speech_recognition/blob/master/examples/microphone_recognition.py
#For reference: https://pypi.org/project/SpeechRecognition/

#You'll need to run 'pip install SpeechRecognition' and 'pip install PyAudio' to make this work

# NOTE: this example requires PyAudio because it uses the Microphone class
import win32com.client as wincl
import speech_recognition as sr
import webbrowser as wb

# Uses Windows built-in voice
speak = wincl.Dispatch("SAPI.SpVoice")

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    speak.Speak("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    words = r.recognize_google(audio)
    speak.Speak("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    wb.open("https://www.youtube.com/results?search_query=" + words)
    
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
