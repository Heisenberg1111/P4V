#! /usr/bin/python3

# First tkinter script
#
# August 27 2020


#Command when a button is clicked

def unClick():
	action.configure(text="Click Me!")
	action.configure(command=clickMe)
	aLabel.configure(foreground='black')
def clickMe():
	action.configure(text="** I have been Clicked! **")
	action.configure(command=unClick)
	aLabel.configure(foreground='red')


import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title("First Tkinter Python Window")

#adding a Label (aLabel is  the object instance of the Label)
aLabel = ttk.Label(win,text="Heading 1")
aLabel.grid(column=0, row=0)

#adding a button (action is the object instance of the button)
action=ttk.Button(win,text="Click Me!", command=clickMe) # Calls the clickMe function when clicked
action.grid(column=1, row=0)


win.mainloop()
