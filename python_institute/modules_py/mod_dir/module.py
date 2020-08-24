#!/usr/bin/python3

""" module.py - an example of Python module """

__counter = 0


def sum1(list):
	
	global __counter
	__counter +=1 
	sum=0
	for i in list:
		sum += i
	return sum


def prod1(list):
	
	global __counter
	__counter+=1
	product=1
	for i in list:
		product *= i
	return product


if __name__ == "__main__":
	print("Initiate Test Sequence. Function in Stand Alone Mode")
	list=[i+1 for i in range(5)]
	print(sum1(list) == 15 )
	print(prod1(list) == 120)
