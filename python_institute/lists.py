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
