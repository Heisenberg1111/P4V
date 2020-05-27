#!/usr/bin/python3

# Calculate a Fibonacci Sequence
#
# May 22 2020


def fibonacci(x):
	global fib_list
	fib_list=[1,1]
	for i in range(x-2):
		
		y=len(fib_list)-2
		z=len(fib_list)-1
		fib_list.append(fib_list[y]+fib_list[z])
	return(fib_list)


print("""
#++++++++++++++++++#
#                  #
# Fibonacci Series #
#	           #
#++++++++++++++++++#
""")

x=int(input("Enter Range:"))

print(fibonacci(x),end="\n\n")
j=0
for i in fib_list:
	
	j+=i

print(j)
