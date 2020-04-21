odd_number=0
even_number=0
counter=0
number=int(input("Enter a Number (0 to exit): "))

#Entering 0 will terminate the while loop
while number!=0:
	counter+=1
	if number%2 == 1:
		odd_number+=1
	elif number%2 == 0:
		even_number+=1
	else:
		print("Not a number")

	number=int(input("Enter a Number (0 to exit): "))

print("\nOdd numbers entered is",odd_number)
print("Even numbers entered is",even_number)
print("Number of iterations before exiting program is", counter)


