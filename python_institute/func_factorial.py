#!/usr/bin/python3

# Program that ask a number and compute its factorial
#
# May 22 2020

def factorial(x):
	
	if x < 0:
		return None
	if x < 2:
		return 1
	j=1

	for i in range(x):
		i=i+1
		j=j*i
	return j


print("""
#########################
#                       #
# Factorial Computation #
#               	#
#########################
""")
while True:
	num=int(input("Enter a Number: "))
	if num==0:
		print("\n#----------END----------#\n")
		break
	print(num, factorial(num))


