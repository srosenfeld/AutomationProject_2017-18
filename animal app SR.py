import pyautogui as pg
import webbrowser

answer = pg.confirm(text="What kind of animal?", title="Choose your animal", buttons=['cats', 'dogs', 'parrots'])


if answer == "cats":
    question2 = pg.confirm("What kind of cat video?","Cat video",["play","sleep","knock stuff over"])
    
    if question2 == "play":
        webbrowser.open("https://www.youtube.com/watch?v=P2RkTCHTLbY")


    elif question2 == "sleep":
        webbrowser.open("https://www.youtube.com/watch?v=P2RkTCHTLbY")

    elif question2 == "knock stuff over":
        webbrowser.open("https://www.youtube.com/watch?v=P2RkTCHTLbY")

elif answer == "dogs":
    question3 = pg.confirm("What kind of dog video?", "Dog video",["play","funny","roll over"])

    if question3 == "play":
        webbrowser.open("https://www.youtube.com/watch?v=zHPTzFM_DU4")

    elif question3 == "funny":
        webbrowser.open("https://www.youtube.com/watch?v=zHPTzFM_DU4")

    elif question3 == "roll over":
        webbrowser.open("https://www.youtube.com/watch?v=zHPTzFM_DU4")
