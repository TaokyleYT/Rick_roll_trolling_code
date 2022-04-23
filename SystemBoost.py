#import stuff
import appJar
from appJar import gui
import pynput
from pynput.keyboard import Listener
from pynput import keyboard
from time import sleep
from random import randint
import webbrowser
import os

#detect keys the target pressed
#can copy from else: to the e() above the next else: to add more keys that trolls the target
def on_press(key):
    if key == Key.shift:
        try:
            e()
        except AttributeError:
            e()
    else:
        if key == Key.shift_r:
            try:
                e()
            except AttributeError:
                e()
        else:
            if key == Key.e:
                try:
                    e()
                except AttributeError:
                    e()
            else:
                if key == Key.r:
                    try:
                        e()
                    except AttributeError:
                        e()
                else:
                    if key == Key.w:
                        try:
                            e()
                        except AttributeError:
                            e()
                    else:
                        if key == Key.i:
                            try:
                                e()
                            except AttributeError:
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
#time to detect if the user click button
with Listener(on_press=on_press) as listener:
    try: 
        listener.join()
    except MyException as e:
        print("oof, things kinda went wrong. {0} was pressed".format(e.args[0]))



