# Creates a 3D Array

# 3 Buildings
#
# 15 Floors
#
# 20 rooms each floor


ROOM = "EMPTY"

r=[ROOM for i in range(14)]

f=[r for j in range(10)]

# print(f)

b=[f for k in range(3)]

# print(b)

# populate the 10th room for each odd floors on all the buildings
floor_counter=0
bldg_cnt=0
for x in b:
	for y in x:
		z=y[:] # Be careful on assigning only the value of the list not the list reference itself
		if floor_counter%2==1:
			z[9]="FULL"
		y=z[:]
		x[floor_counter]=y[:]
		floor_counter+=1
	b[bldg_cnt]=x[:]
	bldg_cnt+=1
	floor_counter=0

print(b)
