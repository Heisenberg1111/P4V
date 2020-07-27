#! /usr/bin/python3

# -----------------------------------
#
# Sample Code for using random module
#
# July 27 2020
#
# -----------------------------------

import random

for i in range(2,5):
	
	random.seed(i)

	for j in range(2,5):
		print("random\n")
		print(random.random(), end=" ")

		print("\nRandRange(end)\n")
		print(random.randrange(j), end=" ")

		print("\nRandRange(beg, end)\n")
		print(random.randrange(j, j+1), end=" ")

		print("\nRandRange(beg, end, step)\n")
		print(random.randrange(j, j+1, 1), end=" ")

	print("\n+++++++++++++++++++++++\n")
