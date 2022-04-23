#import stuff
import appJar
from appJar import gui
import pynput
from pynput.mouse import Listener
from pynput import mouse
from time import sleep
from random import randint
import webbrowser
import os

#detect mouse movement from the target
def on_move(x, y):
    e()

def on_click(x, y, button, pressed):
    if pressed:
        e()

def on_scroll(x, y, dx, dy):
    e()


#code that opens rush E and rick roll, both earrape
def e():
    webbrowser.open("https://www.youtube.com/watch?v=JzvDoyW5u5g")
    webbrowser.open("https://www.youtube.com/watch?v=kLuS72i7Vz8")
    webbrowser.open("https://www.youtube.com/watch?v=JzvDoyW5u5g")
    webbrowser.open("https://www.youtube.com/watch?v=kLuS72i7Vz8")
    webbrowser.open("https://www.youtube.com/watch?v=JzvDoyW5u5g")
    webbrowser.open("https://www.youtube.com/watch?v=kLuS72i7Vz8")
    webbrowser.open("https://www.youtube.com/watch?v=JzvDoyW5u5g")
    webbrowser.open("https://www.youtube.com/watch?v=kLuS72i7Vz8")
    webbrowser.open("https://www.youtube.com/watch?v=JzvDoyW5u5g")
    webbrowser.open("https://www.youtube.com/watch?v=kLuS72i7Vz8")


#code that troll the target even more(or maybe a bit over) by opening tenth to thousands of rick roll and rush E earrape tabs
def crash():
#start deleting if u dont want warning
    print("rlly?")
    sleep(2)
    print("alright, as you wish")
    sleep(2)
    print("oh btw it will ruin your computer unless you use ctrl+alt+del or u lucky")
    sleep(2)
    print("ugh why am I telling you these, juts start the ruining sequence")
    sleep(2)
    print("here you go!")
    sleep(2)
#stop deleting if u dont want warning
    x=0
    y=randint(6, 101)
    while x<y:
        e()
        x=x+1

#creating troll thing(can delete it if u dont want an app to appear, delete till the next #
app = gui()  
app.addLabel("30", "(Shift)E")
app.addButton("E", e)
app.addButton("Destroy me", crash)

app.go()
#stop deleting if u want to delete the troll app, the code under is important for key trolling
#start the listener




