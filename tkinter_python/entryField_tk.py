#! /usr/bin/python3

# Usage of the entry widget
#
# August 27 2020


#Command when a button is clicked
def unClick():
	action.configure(text="Click Me!")
	action.configure(command=clickMe)

def clickMe():
	action.configure(text="Hello "+name.get())
	action.configure(command=unClick)


import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title("First Tkinter Python Window")

#adding a Label (aLabel is  the object instance of the Label)
aLabel = ttk.Label(win,text="Enter your name: ")
aLabel.grid(column=0, row=0)

#adding an Entry field
name = tk.StringVar() #This will serve as the holder of the string value to be written on the Entry field
nameEntry = ttk.Entry(win, width=12, textvariable=name)
nameEntry.grid(column=0, row=1)
nameEntry.focus() #Place a cursor on the entry box as the GUI is called. No need to manually click on the Entry Field
# nameEntry.configure(state='disabled') #disable the entry field

#adding a button (action is the object instance of the button)
action=ttk.Button(win,text="Click Me!", command=clickMe) # Calls the clickMe function when clicked
action.grid(column=1, row=1)
# action.configure(state='disabled') #Disable the Button


win.mainloop()
