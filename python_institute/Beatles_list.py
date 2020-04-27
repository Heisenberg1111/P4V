# List manipulation Exercise

beatles=[]

print("Step 1:",beatles)

beatles.append("John Lennon")
beatles.append("Paul  McCartney")
beatles.append("George Harrison")

print("Step 2:",beatles)

for i in range(2):

	NewName=input("Enter Name (Stu Sutcliffe & Pete Best): ")
	
	beatles.append(NewName)

print("Step 3:",beatles)

del beatles[3]
del beatles[3]

print("Step 4:",beatles)

beatles.insert(3,"Ringo Starr")

print("Step 5:", beatles)
