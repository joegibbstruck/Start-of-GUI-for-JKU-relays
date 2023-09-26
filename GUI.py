## imports
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## hardware
rly1 = LED(23)
rly2 = LED(22)
rly3 = LED(21)
rly4 = LED(20)
rly5 = LED(19)
rly6 = LED(18)
rly7 = LED(17)
rly8 = LED(16)

ALL = [rly1, rly2, rly3, rly4, rly5, rly6, rly7, rly8]





## GUI def
win = Tk()
win.title("18 JKU")
myFont = tkinter.font.Font(family = 'helvetica', size = 12, weight = "bold")

def rly1Toggle():
    if rly1.is_lit:
        rly1.off()
        rly1Button["text"] = "1 OFF"
        rly1Button["bg"] = "green"
    else:
        rly1.on()
        rly1Button["text"] = "1 ON"
        rly1Button["bg"] = "red"

def rly2Toggle():
    if rly2.is_lit:
        rly2.off()
        rly2Button["text"] = "2 OFF"
        rly2Button["bg"] = "green"
    else:
        rly2.on()
        rly2Button["text"] = "2 ON"
        rly2Button["bg"] = "red"

def rly3Toggle():
    if rly3.is_lit:
        rly3.off()
        rly3Button["text"] = "3 OFF"
        rly3Button["bg"] = "green"
    else:
        rly3.on()
        rly3Button["text"] = "3 ON"
        rly3Button["bg"] = "red"

def rly4Toggle():
    if rly4.is_lit:
        rly4.off()
        rly4Button["text"] = "4 OFF"
        rly4Button["bg"] = "green"
    else:
        rly4.on()
        rly4Button["text"] = "4 ON"
        rly4Button["bg"] = "red"

def rly5Toggle():
    if rly5.is_lit:
        rly5.off()
        rly5Button["text"] = "5 OFF"
        rly5Button["bg"] = "green"
    else:
        rly5.on()
        rly5Button["text"] = "5 ON"
        rly5Button["bg"] = "red"

def rly6Toggle():
    if rly6.is_lit:
        rly6.off()
        rly6Button["text"] = "6 OFF"
        rly6Button["bg"] = "green"
    else:
        rly6.on()
        rly6Button["text"] = "6 ON"
        rly6Button["bg"] = "red"

def rly7Toggle():
    if rly7.is_lit:
        rly7.off()
        rly7Button["text"] = "7 OFF"
        rly7Button["bg"] = "green"
    else:
        rly7.on()
        rly7Button["text"] = "7 ON"
        rly7Button["bg"] = "red"

def rly8Toggle():
    if rly8.is_lit:
        rly8.off()
        rly8Button["text"] = "8 OFF"
        rly8Button["bg"] = "green"
    else:
        rly8.on()
        rly8Button["text"] = "8 ON"
        rly8Button["bg"] = "red"

def ALLToggle():
    if ALL.is_lit:
        ALL.off()
        ALLButton["text"] = "ALL OFF"
        ALLButton["bg"] = "green"
    else:
        ALL.on()
        ALLButton["text"] = "ALL ON"
        ALLButton["bg"] = "red"



def close():
    RPi.GPIO.cleanup()
    win.destroy()

## widgets
rly1Button= Button( win, text = 'Relay 1 ON', font = myFont, command = rly1Toggle, bg = 'green', height = 1, width = 24)
rly1Button.grid(row=1, column=0)

rly2Button= Button( win, text = 'Relay 2 ON', font = myFont, command = rly2Toggle, bg = 'green', height = 1, width = 24)
rly2Button.grid(row=1, column=1)

rly3Button= Button( win, text = 'Relay 3 ON', font = myFont, command = rly3Toggle, bg = 'green', height = 1, width = 24)
rly3Button.grid(row=1, column=2)

rly4Button= Button( win, text = 'Relay 4 ON', font = myFont, command = rly4Toggle, bg = 'green', height = 1, width = 24)
rly4Button.grid(row=1, column=3)

rly5Button= Button( win, text = 'Relay 5 ON', font = myFont, command = rly5Toggle, bg = 'green', height = 1, width = 24)
rly5Button.grid(row=2, column=0)

rly6Button= Button( win, text = 'Relay 6 ON', font = myFont, command = rly6Toggle, bg = 'green', height = 1, width = 24)
rly6Button.grid(row=2, column=1)

rly7Button= Button( win, text = 'Relay 7 ON', font = myFont, command = rly7Toggle, bg = 'green', height = 1, width = 24)
rly7Button.grid(row=2, column=2)

rly8Button= Button( win, text = 'Relay 8 ON', font = myFont, command = rly8Toggle, bg = 'green', height = 1, width = 24)
rly8Button.grid(row=2, column=3)

ALLButton= Button( win, text = 'ALL ON', font = myFont, command = ALLToggle, bg = 'green', height = 1, width = 24)
ALLButton.grid(row=6, column=0)

exitButton = Button( win, text = 'exit', font = myFont, command = close, bg = 'red', height = 1, width = 24)
exitButton.grid(row=6, column=1)

## clean close
win.protocol("WM_DELETE_WINDOW", close)
## keeps running
win.mainloop()
