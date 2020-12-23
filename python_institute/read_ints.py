#!/usr/bin/python3

# read ints safely

# December 23 2020

def readint(prompt, min, max):
	
	doit=True

	while doit:
		try:
			num=int(input(prompt))
			assert min<=num and num<=max
			return num	
		except AssertionError:
			print("Error: the value is not within permitted range ( ",min,"..",max, " )")
		except ValueError:
			print("Wrong input")

		

v=readint("Enter a Number from -10 to 10: ",-10,10)

print("The Number is: ", v)
