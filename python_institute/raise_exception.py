#!/usr/bin/python3

# Sept 28 2020

# use raise to simulate an exception

def badFun(n):
	raise ZeroDivisionError


try:
	badFun(0)
except ZeroDivisionError:
	print("Division by Zero")
except:
	print("Something is Wrong")

print("THE END")

