#!/usr/bin/python3

# Create a tabbed widget

# November 27 2020

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

	if radSel == 1: Frame2.configure(text=COLOR1)
	elif radSel == 2: Frame2.configure(text=COLOR2)
	elif radSel == 3: Frame2.configure(text=COLOR3)

def _quit(): # To be called by the Exit menu item (File>>Exit)

	win.quit()
	win.destroy()
	exit()


import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu

COLOR1="Blue"
COLOR2="Gold"
COLOR3="Red"

win=tk.Tk()

win.title("Python GUI")
# win.configure(background='white') #change the background color
win.resizable(0,0)

tabControl=ttk.Notebook(win)

tab1=ttk.Frame(tabControl)
tabControl.add(tab1, text='General')

tab2=ttk.Frame(tabControl)
tabControl.add(tab2, text='Settings')

tabControl.pack(expand=1, fill="both")

main_frame=ttk.LabelFrame(tab1, text='Main Frame')
main_frame.grid(column=0, row=0, padx=10, pady=10)

#adding a Label (aLabel is  the object instance of the Label)
aLabel = ttk.Label(main_frame,text="Enter your name: ") # , background='red'
aLabel.grid(column=0, row=0, sticky='W')

bLabel = ttk.Label(main_frame,text="Choose a Number: ") # , background='red'
bLabel.grid(column=1, row=0)

#adding an Entry field
name = tk.StringVar() #This will serve as the holder of the string value to be written on the Entry field
nameEntry = ttk.Entry(main_frame, width=12, textvariable=name)
nameEntry.grid(column=0, row=1, sticky=tk.W)
nameEntry.focus() #Place a cursor on the entry box as the GUI is called. No need to manually click on the Entry Field
# nameEntry.configure(state='disabled') #disable the entry field

#adding a combo box field
number=tk.StringVar()
numberChosen=ttk.Combobox(main_frame, width=12, textvariable=number) #Create a combo box instance
numberChosen['values']=(1,2,4,42,100) #Initialize a default values for the combo box. Not necessarily the only values
numberChosen.grid(column=1, row=1)
numberChosen.current(0) #Display the first tuple value os the default value when the GUI is launched
numberChosen.configure(state='readonly') #option to restrict the user to choose only on the available values

# New Label Frame for Tab 2

Frame2 = ttk.LabelFrame(tab2, text='Settings Tab')
Frame2.grid(column=0, row=0, padx=10, pady=10)

#adding check button
chVarDis=tk.IntVar()
check1=tk.Checkbutton(Frame2, text="Disabled", variable=chVarDis, state='disable')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W) # sticky tk.W means align left or west

chVarUn=tk.IntVar()
check2=tk.Checkbutton(Frame2, text="Unchecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn=tk.IntVar()
check3=tk.Checkbutton(Frame2, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

#adding radio buttons
radVar=tk.IntVar() #radio buttons having shared IntVar variable will aotumatically deselect other radio buttons when one is selected.
rad1=tk.Radiobutton(Frame2, text=COLOR1, variable=radVar, value=1, command=radCall)
rad1.grid(column=0, row=5, sticky=tk.W)

rad2=tk.Radiobutton(Frame2, text=COLOR2, variable=radVar, value=2, command=radCall)
rad2.grid(column=1, row=5, sticky=tk.W)

rad3=tk.Radiobutton(Frame2, text=COLOR3, variable=radVar, value=3, command=radCall)
rad3.grid(column=2, row=5, sticky=tk.W)

#adding a scrolled text entry
scrolW=50
scrolH=5
scr=scrolledtext.ScrolledText(main_frame, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3, sticky='WE')

#adding a button (action is the object instance of the button)
action=ttk.Button(main_frame,text="Click Me!", command=clickMe) # Calls the clickMe function when clicked
action.grid(column=2, row=1)
# action.configure(state='disabled') #Disable the Button

#adding a labelFrame
labelsFrame=ttk.LabelFrame(Frame2, text="This is a Label Frame")
labelsFrame.grid(column=0, row=7, padx=10, pady=20)

for i in range(3): # Create 3 Lables within the labels Frame
	
	ttk.Label(labelsFrame, text="Col "+str(i+1)+" Label Frame").grid(column=0, row=i)


# addition of the menu bar
menuBar=Menu(win) # create instance of menu and attach it to the main GUI window
win.config(menu=menuBar) # make the instance of menuBar the menu of the main GUI

fileMenu=Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu) # The File menu created from the menuBar instance. The fileMenu will then be the child of this "File" label

aboutMenu=Menu(menuBar, tearoff=0)
aboutMenu.add_command(label='About')
menuBar.add_cascade(label='Help', menu=aboutMenu)



win.mainloop()
