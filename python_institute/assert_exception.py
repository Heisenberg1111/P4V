#!/usr/bin/python3

# Sept 28 2020

# Demonstrate the use of assert
# assert <expression> - used to filter out unwanted or wrong data to be processed and yield invalid results

import math
x = float(input("Enter a Number: "))

try:
	assert x >= 0.0
	x=math.sqrt(x)
	print(x)
except AssertionError:
	print("Number Cannot be negative")


print("END OF SCRIPT")


