# Remove the duplicate elements on a given list

ogList=[1,2,4,4,1,4,2,6,2,9]

numFind = 0
counter = 0

print("\nList with Duplicate:",ogList,"\n")

for i in ogList:
	
	numFind = i
	
	while numFind in ogList[counter+1:]:
		
		for j in range(counter+1,len(ogList)):
			
			if numFind == ogList[j]:
				del ogList[j]
				break
	counter+=1


print("\nList with no Duplicate:",ogList,"\n")
