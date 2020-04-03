import time

name="Pan"

x=0
#name=input("What is your Name: ")
localtime=time.asctime(time.localtime(time.time()))
print ("Time Log: ", localtime)

if name=="Pan":
	while x<11:
	 print("Hello Pan")
	 time.sleep(1)
	 x+=1
else:

	while x<11:
 	 print("Hello " + name)
 	 time.sleep(1)
 	 x+=1

