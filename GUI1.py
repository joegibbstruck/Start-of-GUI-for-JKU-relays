## imports
from tkinter import *
import tkinter.font
import tkinter
from gpiozero import LED
from gpiozero import LEDBoard



## hardware

allrlys= LEDBoard(rly1=23, rly2=22, rly3=21, rly4=20, rly5=19, rly6=18, rly7=17, rly8=16)


## definitions
def close():
        allrlys.close()
        win.destroy()

def shutdown():
        check_call(['sudo', 'poweroff'])

def rly1():

   if rly1.is_lit:
        rly1.off()
        rly1Button["text"] = "8 OFF"
        rly1Button["bg"] = "green"
   else:
        rly1.on()
        rly1Button["text"] = "8 ON"
        rly1Button["bg"] = "red"





## gui setup
win = Tk()
win.title("18 JKU")
myFont = tkinter.font.Font(family = 'helvetica', size = 12, weight = "bold")

## widgets
rly1Button = Button( win, text = "Relay 1 ON", font = myFont, command = allrlys.rly1.toggle, bg = 'green', height = 1, width = 24)
rly1Button.grid(row=1, column=0)

rly2Button = Button( win, text = 'Relay 2 ON', font = myFont, command = allrlys.rly1.toggle , bg = 'green', height = 1, width = 24)
rly2Button.grid(row=1, column=1)

rly3Button = Button( win, text = 'Relay 3 ON', font = myFont, command = allrlys.rly3.toggle , bg = 'green', height = 1, width = 24)
rly3Button.grid(row=1, column=2)

rly4Button = Button( win, text = 'Relay 4 ON', font = myFont, command = allrlys.rly4.toggle , bg = 'green', height = 1, width = 24)
rly4Button.grid(row=1, column=3)

rly5Button = Button( win, text = 'Relay 5 ON', font = myFont, command = allrlys.rly5.toggle , bg = 'green', height = 1, width = 24)
rly5Button.grid(row=2, column=0)

rly6Button = Button( win, text = 'Relay 6 ON', font = myFont, command = allrlys.rly6.toggle , bg = 'green', height = 1, width = 24)
rly6Button.grid(row=2, column=1)

rly7Button = Button( win, text = 'Relay 7 ON', font = myFont, command = allrlys.rly7.toggle , bg = 'green', height = 1, width = 24)
rly7Button.grid(row=2, column=2)

rly8Button = Button( win, text = 'Relay 8 ON', font = myFont, command = allrlys.rly8.toggle , bg = 'green', height = 1, width = 24)
rly8Button.grid(row=2, column=3)

allrlysButton = Button( win, text = 'ALL ON', font = myFont, command = allrlys.on , bg = 'green', height = 1, width = 24)
allrlysButton.grid(row=3, column=0)

allrlysButton = Button( win, text = 'ALL OFF', font = myFont, command = allrlys.off , bg = 'green', height = 1, width = 24)
allrlysButton.grid(row=3, column=1)

exitButton = Button( win, text = 'exit', font = myFont, command = close, bg = 'red', height = 1, width = 24)
exitButton.grid(row=3, column=2)

SHUTDOWNButton = Button( win, text = 'SHUTDOWN', font = myFont, command = shutdown, bg = 'red', height = 1, width = 24)
SHUTDOWNButton.grid(row=3, column=3)

## clean close
win.protocol("WM_DELETE_WINDOW", close)

## keeps running
win.mainloop()