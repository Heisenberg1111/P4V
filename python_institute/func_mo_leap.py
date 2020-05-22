#!/usr/bin/python3

# Determines if a year is a leap year or not
#
# Calculates the number of Days a month has on that year
	
def lpyear(year):

	if year>=1582:
		if (year%4)!=0:
			return False
		elif (year%100)!=0:
			return True
		elif (year%400)!=0:
			return False
		else:
			return True


	else:
		return False


def monthdays(year,month):

	isLeap=lpyear(year)

	if month==2:
		
		if isLeap==True:
			days=29
		else:
			days=28
	elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
		days=31
	elif month==4 or month==6 or month==9 or month==11:
		days=30
	else:
		return None
	
	return days

print("\nExercise for Using Functions with Parameters\n")

yr=int(input("Enter a Year: "))
mt=int(input("Enter a Month(1-12): "))


dy=monthdays(yr,mt)

print("The Month of", mt, "on year",yr, "has",dy,"days")
