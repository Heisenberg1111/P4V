#!/usr/bin/python3


# Basic Functionality of the try and except block.
# September 9 2020


firstNumber=int(input("Enter First Number: "))
secondNumber=int(input("Enter Second Number: "))

try:
	print(firstNumber//secondNumber)
	# If user input 0 as second number, the ZeroDivisionError
	# error will occur
except: # Except block will be called when ZeroDivisionError exception has been raised
	print("This Action Cannot be Done.")


print("THE END")
