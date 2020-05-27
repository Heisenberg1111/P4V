#!/usr/bin/python3

# Program to Enter a Key and Print out value from a dictionary
#
# Determines if the key exists or not first
#


dict={"cat":"pusa","dog":"aso","horse":"kabayo","goat":"kambing","cow":"baka", \
"monkey":"unggoy","bird":"ibon","fish":"isda","spider":"gagamba"}

print("""
#++++++++++++++++++++++#
#                      #
# What is the Filipino #
# term for that?       #
#                      #
# Type EXIT to exit    #
#                      #
#++++++++++++++++++++++#
""")

while True:
	valKey=input("Enter Animal name in English: ")

	valKey=valKey.lower()
	
	if valKey=="exit":
		print("\n#++++++++++END of PROGRAM++++++++++#\n")
		break
	else:
		if valKey in dict:
			print(valKey+" in Filipino is",dict[valKey]+"\n")
		else:
			print("Word not Yet in Dictionary\n")


for tg in sorted(dict.keys()): # Prints all the key-value pair in the dictionary using keys() function

	print(tg, "->",dict[tg])

print("\n")

print("Using items() and its output Tuples\n")

for eng in dict.items():

	print(eng)

print("\n")
