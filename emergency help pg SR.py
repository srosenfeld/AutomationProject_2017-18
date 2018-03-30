import pyautogui as pg
import webbrowser
import time

emergency = pg.prompt(
    """
What is your emergency?
a)Weather/Natural Disaster
b)Health (i.e. choking, heart attack, etc.)
c)Safety (i.e. burglary)

""")

if emergency == "a":
    category = pg.prompt(
        """
What kind of weather/natural disaster incident?
a)Fire
b)Flood
c)Hurricane
d)Snowstorm/Blizzard

        """)

elif emergency == "b":
    category = pg.prompt(
        """
What kind of health-related emergency?
a)Choking
b)Heart attack
c)Allergic reaction

""")
    
pg.alert("""
If you are in immediate danger, please call 911 immediately.
Follow the instructions in the webpages that open following this message for other guidance.
""")
if emergency == "a":
    if category == "a":
        webbrowser.open("http://www.redcross.org/get-help/how-to-prepare-for-emergencies/types-of-emergencies/fire/if-a-fire-starts")
    elif category == "b":
        webbrowser.open("https://www.ready.gov/floods")

elif emergency == "b":
    if category == "a":
        webbrowser.open("https://www.youtube.com/watch?v=PA9hpOnvtCk")
    elif category == "b":
        webbrowser.open("https://www.mayoclinic.org/first-aid/first-aid-heart-attack/basics/art-20056679")
