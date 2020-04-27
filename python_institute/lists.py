#lists
numbers=[10,5,7,2,3]

#accessing and changing a list element. List is zero-indexed.
numbers[2]=int(input("enter number: "))

#accessing list using negative values
print(numbers[-2])

print(numbers)

#determining the length of the list

list_len=len(numbers)
print("List Length is:",list_len)

#deleting a list element

del numbers[0]
print("New List:",numbers,"\nWith Length: " + str(len(numbers)),"\n")


#List Methods

# 1. Append() - Append a value to the end of the list

numbers.append(888)
print("Appended list:",numbers)
print("Appended List Length:",len(numbers),"\n")

# 2. insert(location, value) - Insert a value at specified location

num_insert=int(input("Enter Number to insert in List Index 1: " ))
numbers.insert(1,num_insert)
print("New List with " + str(num_insert)+" inserted:",numbers,"\n")


# 3. Initializing an empty list

myList=[]
myInsert=[]

for i in range(8):

	myList.append(i+1)
	myInsert.insert(0,i+1)

print(myList)
print(myInsert)
