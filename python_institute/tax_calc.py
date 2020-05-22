income=float(input("Enter Annual Income: "))


tax=0.0

if income<=85528:
	tax=(income*0.18)-556.02
	tax=round(tax,2)
	if tax<=0:
		tax=0.0
else:
	tax=((income-85528)*0.32)+14839.02
	tax=round(tax,2)

tax=round(tax,0)
print("Tha tax is:",tax,"Thalers")
