# Search an element in the list and determine its index

myList = [0,1,2,3,4,5,6,7,8,9,10]

del myList[0]
myList.reverse()

toFind = int(input("What number to find ( 0 to 10 )? "))

counter=0

if toFind in myList:

	for i in myList:
		
		if i == toFind:
			
			print("Found it!", toFind, "is in index", counter, "\n")
			break
		counter+=1

else:
	print("\nNumber you Entered is not in the List\n")


print("\n***************************************\n")
