year = int(input("Enter Year: "))

if year>=1582:
	if (year%4)!=0:
		print("Common Year")
	elif (year%100)!=0:
		print("Leap Year")
	elif (year%400)!=0:
		print("Common Year")
	else:
		print("Leap Year")


else:
	print("Not Within the Gregorian Era")
