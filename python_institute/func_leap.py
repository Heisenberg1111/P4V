# Determines if a year is a leap year or not
#
# Creates a function which calculate if year is leap or not
	
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


yearData=[1900,2000,2016,1987]

print("\nExercise for Using Functions with Parameters\n")

for i in range(len(yearData)):
	
	yr=yearData[i]
	print(yr,"->",end="")
	res=lpyear(yr)
	if res==True:
		print("OK")
	else:
		print("FAILED")
