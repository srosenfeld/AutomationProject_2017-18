import pyautogui as pg
import time
import webbrowser

#Ask a question
charity = pg.prompt(
    """
Which cause would you like to help today?
a)save the environment
b)help end poverty
c)improve access to education for all
d)protect animals

""")

method = pg.prompt(
    """
How would you like to help today?
a)donate
b)volunteer
c)spread the word

""")

pg.alert("You can help this cause using the site(s) that will open now.")

if charity == "a":
    webbrowser.open("https://www.charitynavigator.org/index.cfm?bay=search.categories&categoryid=4")
    webbrowser.open("https://www.nrdc.org/")
elif charity == "b":
    webbrowser.open("https://www.oxfamamerica.org/")
    
    
    
