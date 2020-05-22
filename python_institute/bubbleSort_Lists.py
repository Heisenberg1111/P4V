# Sorting a list using the traditional bubble sort
#
# Bubble sort as in having the values bubble or float upwards depending on the sorting condition
#

myList=[10,99,45,123,89,69,55]

print("\nInitial List: ",myList)

print(
"""
+=============================+
|                             |
|         Bubble Sort         |
|                             | 
| Press 1 for increasing Sort |
|                             |
| Press 2 for decreasing Sort |
|                             |
| Press 3 for Reverse         |
|                             |
+=============================+
""")

mySort=int(input("\nEnter Desired Sorting: "))

if mySort == 1:
	for i in range(len(myList)):

		for i in range(len(myList)-1):
		
			if myList[i] > myList[i+1]:
				myList[i], myList[i+1]=myList[i+1],myList[i]
	print("\nList in Increasing Order:",myList,"\n")

elif mySort == 2:
	for i in range(len(myList)):
		for i in range(len(myList)-1):
		
			if myList[i] < myList[i+1]:
				myList[i],myList[i+1]=myList[i+1],myList[i]
	print("\nList in Decreasing Order:",myList,"\n")
elif mySort == 3:
	
	myList.reverse()
	print("\nList in Reverse Order:",myList,"\n")

else:
	print("\nWrong Code Entered.Try Again\n")
