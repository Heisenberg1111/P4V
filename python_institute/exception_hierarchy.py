#!/usr/bin/python3

# Demonstrate the effect of Exception hierarchy on exception handling
# ZeroDivisionError is a more specific exception of the ArithmeticError 




try:
	y=1/0
except ZeroDivisionError:
	print("Zero Division")
except ArithmeticError:
	print("Arithmetic Problem")

print("THE END")
