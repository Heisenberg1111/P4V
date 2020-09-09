#!/usr/bin/python3


try:
	x=int(input("Enter a Number: ")) # ValueError Exception is raised when a non-numeric character is entered
	y=1/x #ZeroDivisionError exception is raised when x is equal to zero
	print(y)
except ZeroDivisionError:
	print("Cannot Divide by Zero")
except ValueError:
	print("Enter a number only")
except: 
	print("Something went wrong")

print("THE END")
