import pyautogui as pg
import webbrowser
import time

mood = pg.prompt(
    """
How would you describe your mood?
a)Happy
b)Sad
c)Angry
d)Bored

""")

if mood == "a":
    answer = pg.prompt(
        """
Glad to hear you're happy! What are you up to today?
""")
    pg.alert("I hope you enjoy: " + answer)
    pg.alert("Here's a fun video to keep you smiling!")
    webbrowser.open("https://www.youtube.com/watch?v=ZbZSe6N_BXs")


elif mood == "b":
    answer = pg.prompt(
        """
I'm sorry you're sad. Any particular reason?

""")
    pg.alert("I hope this will make you feel a little better.")
    webbrowser.open("https://www.youtube.com/watch?v=MBRqu0YOH14")

    
