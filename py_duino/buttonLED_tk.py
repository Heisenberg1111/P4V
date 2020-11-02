#! /usr/bin/python3

# First tkinter script
#
# August 27 2020


#Command when a button is clicked

def unClick():
	time.sleep(0.1)
	ser.write(b'L')
	action.configure(text="LED is OFF")
	action.configure(command=clickMe)
	aLabel.configure(foreground='black')
def clickMe():
	time.sleep(0.1)
	ser.write(b'L')
	time.sleep(0.4)
	ser.write(b'R')
	action.configure(text="RED LED is ON")
	action.configure(command=unClick)
	aLabel.configure(foreground='red')

def unClickGreen():
	time.sleep(0.1)
	ser.write(b'L')
	green.configure(text="LED is OFF")
	green.configure(command=ledGreen)
	bLabel.configure(foreground='black')
def ledGreen():
	time.sleep(0.1)
	ser.write(b'L')
	time.sleep(0.4)
	ser.write(b'G')
	green.configure(text="GREEN LED is ON")
	green.configure(command=unClickGreen)
	bLabel.configure(foreground='green')

def unClickBlue():
	time.sleep(0.1)
	ser.write(b'L')
	blue.configure(text="LED is OFF")
	blue.configure(command=ledBlue)
	cLabel.configure(foreground='black')
def ledBlue():
	time.sleep(0.1)
	ser.write(b'L')
	time.sleep(0.4)
	ser.write(b'B')
	blue.configure(text="BLUE LED is ON")
	blue.configure(command=unClickBlue)
	cLabel.configure(foreground='blue')


import tkinter as tk
import serial
import time
from tkinter import ttk

ser = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)

win = tk.Tk()

win.title("RGB Buttons")

#adding a Label (aLabel is  the object instance of the Label)
aLabel = ttk.Label(win,text="Turn ON RED")
aLabel.grid(column=0, row=0)

bLabel = ttk.Label(win,text="Turn ON GREEN")
bLabel.grid(column=0, row=1)

cLabel = ttk.Label(win,text="Turn ON BLUE")
cLabel.grid(column=0, row=2)

#adding a button (action is the object instance of the button)
action=ttk.Button(win,text="Click Me!", command=clickMe) # Calls the clickMe function when clicked
action.grid(column=1, row=0)

green=ttk.Button(win, text="LED is OFF", command=ledGreen) #turn On the Green LED
green.grid(column=1, row=1)

blue=ttk.Button(win, text="LED is OFF", command=ledBlue) #turn On the Blue LED
blue.grid(column=1, row=2)


win.mainloop()
