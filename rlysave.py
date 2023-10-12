## imports
from tkinter import *
import tkinter.font
import tkinter
from PIL import ImageTk,Image
import os
## create main window
win = Tk()
win.title("18 JKU")
win.geometry("500x300")
## add icon to window make an ICo file and use anything you want
win.iconbitmap('c:/Users/jwhitten/Python_Stuff/jeep.ICO')
## create font
myFont = tkinter.font.Font(family = 'helvetica', size = 12, weight = "bold")
## make and define list of leds use led board, need to readd all gpio data, took out to test on windows computer
leds= (23)
leds_state = True
##define functions for swicthes on main page corrispond with GPIO outputs
def toggle1():
    if rly1.config('text') [-1]==  (content1 + (' ON')):
        rly1.config(text=(content1  + (' OFF')), bg = 'green')  
    else:
    	rly1.config(text=(content1 + (' ON')), bg = 'red' )    	
def toggle2():
    if rly2.config('text') [-1]==  (content2 + (' ON')):
        rly2.config(text=(content2  + (' OFF')), bg = 'green')  
    else:
    	rly2.config(text=(content2 + (' ON')), bg = 'red' )
def toggle3():
    if rly3.config('text') [-1]==  (content3 + (' ON')):
        rly3.config(text=(content3  + (' OFF')), bg = 'green')  
    else:
    	rly3.config(text=(content3 + (' ON')), bg = 'red' )
def toggle4():
    if rly4.config('text') [-1]==  (content4 + (' ON')):
        rly4.config(text=(content4  + (' OFF')), bg = 'green')  
    else:
    	rly4.config(text=(content4 + (' ON')), bg = 'red' )
def toggle5():
    if rly5.config('text') [-1]==  (content5 + (' ON')):
        rly5.config(text=(content5  + (' OFF')), bg = 'green')  
    else:
    	rly5.config(text=(content5 + (' ON')), bg = 'red' )
def toggle6():
    if rly6.config('text') [-1]==  (content6 + (' ON')):
        rly6.config(text=(content6  + (' OFF')), bg = 'green')  
    else:
    	rly6.config(text=(content6 + (' ON')), bg = 'red' )
def toggle7():
    if rly7.config('text') [-1]==  (content7 + (' ON')):
        rly7.config(text=(content7  + (' OFF')), bg = 'green')  
    else:
    	rly7.config(text=(content7 + (' ON')), bg = 'red' )
def toggle8():
    if rly8.config('text') [-1]==  (content8 + (' ON')):
        rly8.config(text=(content8  + (' OFF')), bg = 'green')  
    else:
    	rly8.config(text=(content8 + (' ON')), bg = 'red' )
## turns off all switches reguardless of states
def OFF():
    global leds_state
    if leds_state == True:     
        rly1.config(text =(content1 + (' OFF')), bg= "green")
        rly2.config(text =(content2 + (' OFF')), bg= "green")
        rly3.config(text =(content3 + (' OFF')), bg= "green")
        rly4.config(text =(content4 + (' OFF')), bg= "green")
        rly5.config(text =(content5 + (' OFF')), bg= "green")
        rly6.config(text =(content6 + (' OFF')), bg= "green")
        rly7.config(text =(content7 + (' OFF')), bg= "green")
        rly8.config(text =(content8 + (' OFF')), bg= "green")
        rlyon.config( bg = "green")
    else:
    	leds_state = False
    	rly1.config( text = (content1 + (' ON')), bg = "red")
    	rly2.config( text = (content2 + (' ON')), bg = "red")
    	rly3.config( text = (content3 + (' ON')), bg = "red")
    	rly4.config( text = (content4 + (' ON')), bg = "red")
    	rly5.config( text = (content5 + (' ON')), bg = "red")
    	rly6.config( text = (content6 + (' ON')), bg = "red")
    	rly7.config( text = (content7 + (' ON')), bg = "red")
    	rly8.config( text = (content8 + (' ON')), bg = "red")
    	rlyon.config( bg = "red")
## use this for linking switches, how can i do this VIA gui selection??
def ON():
	global leds_state
	if leds_state == True:
		rly1.config( text =(content1 + (' ON')), bg = "red")
		rly2.config( text =(content2 + (' ON')), bg = "red")
		rly3.config( text =(content3 + (' ON')), bg = "red")
		rly4.config( text =(content4 + (' ON')), bg = "red")
		rly5.config( text =(content5 + (' ON')), bg = "red")
		rly6.config( text =(content6 + (' ON')), bg = "red")
		rly7.config( text =(content7 + (' ON')), bg = "red")
		rly8.config( text =(content8 + (' ON')), bg = "red")
		rlyon.config( bg = "red")
	else:
		leds_state = False
		rly1.config(text = (content1 + (' OFF')), bg= "green")
		rly2.config(text = (content2 + (' OFF')), bg= "green")
		rly3.config(text = (content3 + (' OFF')), bg= "green")
		rly4.config(text = (content4 + (' OFF')), bg= "green")
		rly5.config(text = (content5 + (' OFF')), bg= "green")
		rly6.config(text = (content6 + (' OFF')), bg= "green")
		rly7.config(text = (content7 + (' OFF')), bg= "green")
		rly8.config(text = (content8 + (' OFF')), bg= "green")
		rlyon.config( bg = "red")
## closes window but leave pi on
def close():        
        win.destroy()
## shutsdown pi until repower
def shutdown():
        os.system("sudo shutdown -h now")
## define button for submitt setup
## how do i create a .txt file if one does not exist, without having to add one in the folder?
## is there a way to store this in a list ( to shorten code) or 1 file and refence that one list / file??
def submit():	
	try:
		f=open('switch1.txt','w')
		f.write(textbox1.get())
	except Exception as e:
		print("Error:",str(e))
	finally:
		f.close()
	try:
		f1=open('switch2.txt','w')
		f1.write(textbox2.get())
	except Exception as e:
		print("Error:",str(e))
	finally:
		f1.close()
	try:
		f2=open('switch3.txt','w')
		f2.write(textbox3.get())
	except Exception as e:
		print("Error:",str(e))
	finally:
		f2.close()
	try:
		f3=open('switch4.txt','w')
		f3.write(textbox4.get())
	except Exception as e:
		print("Error:",str(e))
	finally:
		f3.close()
	try:
		f4=open('switch5.txt','w')
		f4.write(textbox5.get())
	except Exception as e:
		print("Error:",str(e))
	finally:
		f4.close()
	try:
		f5=open('switch6.txt','w')
		f5.write(textbox6.get())
	except Exception as e:
		print("Error:",str(e))
	finally:
		f5.close()
	try:
		f6=open('switch7.txt','w')
		f6.write(textbox7.get())
	except Exception as e:
		print("Error:",str(e))
	finally:
		f6.close()
	try:
		f7=open('switch8.txt','w')
		f7.write(textbox8.get())
	except Exception as e:
		print("Error:",str(e))
	finally:
		f7.close()
## change text on buttons immediatly
	rly1.config(text = (textbox1.get() + (" ON")))
	rly2.config(text = (textbox2.get() + (" ON")))
	rly3.config(text = (textbox3.get() + (" ON")))
	rly4.config(text = (textbox4.get() + (" ON")))
	rly5.config(text = (textbox5.get() + (" ON")))
	rly6.config(text = (textbox6.get() + (" ON")))
	rly7.config(text = (textbox7.get() + (" ON")))
	rly8.config(text = (textbox8.get() + (" ON")))
## close setup window
## how do i force restart after clicking submitt, if not restared the text changes back to previous until restarted and refences the .txt files
	win1.destroy()
## define setup menu
def create():
## maybe I can create a list and make one list global?
    global win1
    global texts
    global textboxes
    global text2
    global textbox2
    global text3
    global textbox3
    global text4
    global textbox4
    global text5
    global textbox5
    global text6
    global textbox6
    global text7
    global textbox7
    global text8
    global textbox8
## create new window for setup
    win1 = Toplevel()
    win1.title("SETUP")
    win1.geometry("500x300")    
## define what the text entries are
    text1 = StringVar()
    text2 = StringVar()
    text3 = StringVar()
    text4 = StringVar()
    text5 = StringVar()
    text6 = StringVar()
    text7 = StringVar()
    text8 = StringVar()
## make text entry boxes and corrsponding labels in menu
    textbox1= Entry(win1, textvariable=text1, font = myFont, relief = SUNKEN, width = 10)
    textbox1.grid(row=0, column=0)
    label1=Label(win1, text = "SWITCH #1", font = myFont, width = 10)
    label1.grid(row = 1, column = 0)
    textbox2= Entry(win1, textvariable=text2, font = myFont, relief = SUNKEN, width = 10)
    textbox2.grid(row=0, column=1)
    label2=Label(win1, text = "SWITCH #2", font = myFont, width = 10)
    label2.grid(row = 1, column = 1)
    textbox3= Entry(win1, textvariable=text3, font = myFont, relief = SUNKEN, width = 10)
    textbox3.grid(row=0, column=2)
    label3=Label(win1, text = "SWITCH #3", font = myFont, width = 10)
    label3.grid(row = 1, column = 2)
    textbox4= Entry(win1, textvariable=text4, font = myFont, relief = SUNKEN, width = 10)
    textbox4.grid(row=0, column=3)
    label4=Label(win1, text = "SWITCH #4", font = myFont, width = 10)
    label4.grid(row = 1, column = 3)
    textbox5= Entry(win1, textvariable=text5, font = myFont, relief = SUNKEN, width = 10)
    textbox5.grid(row=3, column=0)
    label5=Label(win1, text = "SWITCH #5", font = myFont, width = 10)
    label5.grid(row = 4, column = 0)
    textbox6= Entry(win1, textvariable=text6, font = myFont, relief = SUNKEN, width = 10)
    textbox6.grid(row=3, column=1)
    label6=Label(win1, text = "SWITCH #6", font = myFont, width = 10)
    label6.grid(row = 4, column = 1)
    textbox7= Entry(win1, textvariable=text7, font = myFont, relief = SUNKEN, width = 10)
    textbox7.grid(row=3, column=2)
    label7=Label(win1, text = "SWITCH #7", font = myFont, width = 10)
    label7.grid(row = 4, column = 2)
    textbox8= Entry(win1, textvariable=text8, font = myFont, relief = SUNKEN, width = 10)
    textbox8.grid(row=3, column=3)
    label8=Label(win1, text = "SWITCH #8", font = myFont, width = 10)
    label8.grid(row = 4, column = 3)
## make the submitt button, update names and files
    submit1 = Button(win1, text="SUBMIT", font = myFont, widt = 10, command = submit, width = 40)
    submit1.grid(row =5, column=0, columnspan = 4)
## define the inputs to refence for button labels
## some way to pull from a single file?
input1 = open('switch1.txt', 'r')
content1 = input1.read()
input1.close
input2 = open('switch2.txt', 'r')
content2 = input2.read()
input2.close
input3 = open('switch3.txt', 'r')
content3 = input3.read()
input3.close
input4 = open('switch4.txt', 'r')
content4 = input4.read()
input4.close
input5 = open('switch5.txt', 'r')
content5 = input5.read()
input5.close
input6 = open('switch6.txt', 'r')
content6 = input6.read()
input6.close
input7 = open('switch7.txt', 'r')
content7 = input7.read()
input7.close
input8 = open('switch8.txt', 'r')
content8 = input8.read()
input8.close
## create relay buttons on main page
rly1 = Button(text = (content1 + (" OFF")), font = myFont, bg = 'green', width=10, command=toggle1)
rly1.grid(row=1, column =0)
rly2 = Button(text = (content2 +(" OFF")), font = myFont, bg = 'green', width=10, command=toggle2)
rly2.grid(row=1, column =1)
rly3 = Button(text = (content3 + (" OFF")), font = myFont, bg = 'green', width=10, command=toggle3)
rly3.grid(row=1, column =2)
rly4 = Button(text = (content4 + (" OFF")), font = myFont, bg = 'green', width=10, command=toggle4)
rly4.grid(row=1, column =3)
rly5 = Button(text = (content5 + (" OFF")), font = myFont, bg = 'green', width=10, command=toggle5)
rly5.grid(row=2, column =0)
rly6 = Button(text = (content6 + (" OFF")), font = myFont, bg = 'green', width=10, command=toggle6)
rly6.grid(row=2, column =1)
rly7 = Button(text = (content7 + (" OFF")), font = myFont, bg = 'green', width=10, command=toggle7)
rly7.grid(row=2, column =2)
rly8 = Button(text = (content8 + (" OFF")), font = myFont, bg = 'green', width=10, command=toggle8)
rly8.grid(row=2, column =3)
## kills all relays
rlyoff = Button(text="ALL OFF", font = myFont, bg = 'green', width=10, command=OFF)
rlyoff.grid(row=3, column =0)
## links multple switches, how can i do this via gui selection??
rlyon = Button(text="ALL ON", font = myFont, bg = 'green', width=10, command=ON)
rlyon.grid(row=3, column =1)
## button for new window for setup
label_rlys = Button(text="setup", font = myFont, bg = 'grey', width =10, command = create)
label_rlys.grid(row=4, column = 0)
## closes just the window
exitbutton = Button(text="EXIT", font = myFont, bg = 'green', width=10, command=close)
exitbutton.grid(row=3, column =2)
## button to shut dowmn rasberry pi prior to shutting truck off
shutdown = Button(text="SHUTDOWN", font = myFont, bg = 'green', width=10, command=shutdown)
shutdown.grid(row=3, column =3)
## close whole window cleanly 
win.protocol("WM_DELETE_WINDOW", close)
## keep running
win.mainloop()

## figure out how to make program boot on start up
## anyway to remove close and minimize button on window? (looks goofy)
## maybe add a button for night mode, or is there a way to use slider to dim screen on rasberry pi 5" touch screen?
## pair with bluetooth on rasberry pi
## use gpio inputs and ( some sensor) to monitor voltage of both batteries and give alarm when low
## use gpio inputs and (some sensor) to monitor current of each swicth
## use GPIO input and ( some sensor) to show cooler temp. and give alarm when high
## what should I use to link rasberry pi on dash to relay board under hood? pi tp pi zero and rs485 / ethernet?
## can I run HP Tuners off the pi?
## if i use solid state relays i can decrease the total size of the underhood relay module
## if i use mos fet I can use PWM for strobe as well as brighness control of output lights.( maybe can monitor amperage with certain ones)
## make a mometary switch to run winch in and out.... non latching, do i even trust a touch screen switch for the winch??
## make a data screen to show live data, press button to change to relay command panel. 
## can i program for up to 24 relays and just hide code in the background if not used?
