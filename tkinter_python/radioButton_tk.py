#! /usr/bin/python3

# Usage of radio buttons
#
# Changing the background color of the GUI
#
# August 27 2020


#Command when a button is clicked
def unClick():
	action.configure(text="Click Me!")
	action.configure(command=clickMe)

def clickMe():
	action.configure(text="Hello "+name.get() +" Queue Number: " + number.get())
	action.configure(command=unClick)

#command when a radio button has been selected
def radCall():
	radSel=radVar.get()

	if radSel == 1: win.configure(background=COLOR1)
	elif radSel == 2: win.configure(background=COLOR2)
	elif radSel == 3: win.configure(background=COLOR3)

import tkinter as tk
from tkinter import ttk

COLOR1="Blue"
COLOR2="Gold"
COLOR3="Red"

win = tk.Tk()

win.title("First Tkinter Python Window")
# win.configure(background='white') #change the background color

#adding a Label (aLabel is  the object instance of the Label)
aLabel = ttk.Label(win,text="Enter your name: ")
aLabel.grid(column=0, row=0)

bLabel = ttk.Label(win,text="Choose a Number: ")
bLabel.grid(column=1, row=0)

#adding an Entry field
name = tk.StringVar() #This will serve as the holder of the string value to be written on the Entry field
nameEntry = ttk.Entry(win, width=12, textvariable=name)
nameEntry.grid(column=0, row=1)
nameEntry.focus() #Place a cursor on the entry box as the GUI is called. No need to manually click on the Entry Field
# nameEntry.configure(state='disabled') #disable the entry field

#adding a combo box field
number=tk.StringVar()
numberChosen=ttk.Combobox(win, width=12, textvariable=number) #Create a combo box instance
numberChosen['values']=(1,2,4,42,100) #Initialize a default values for the combo box. Not necessarily the only values
numberChosen.grid(column=1, row=1)
numberChosen.current(0) #Display the first tuple value os the default value when the GUI is launched
numberChosen.configure(state='readonly') #option to restrict the user to choose only on the available values

#adding check button
chVarDis=tk.IntVar()
check1=tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disable')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W) # sticky tk.W means align left or west

chVarUn=tk.IntVar()
check2=tk.Checkbutton(win, text="Unchecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn=tk.IntVar()
check3=tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

#adding radio buttons
radVar=tk.IntVar() #radio buttons having shared IntVar variable will aotumatically deselect other radio buttons when one is selected.
rad1=tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=radCall)
rad1.grid(column=0, row=5, sticky=tk.W)

rad2=tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall)
rad2.grid(column=1, row=5, sticky=tk.W)

rad3=tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=radCall)
rad3.grid(column=2, row=5, sticky=tk.W)

#adding a button (action is the object instance of the button)
action=ttk.Button(win,text="Click Me!", command=clickMe) # Calls the clickMe function when clicked
action.grid(column=2, row=1)
# action.configure(state='disabled') #Disable the Button


win.mainloop()