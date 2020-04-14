#Compute for the Hypotenuse
#
#c**2=a**2+b**2 (a and b is always positive)
#
# Rev1: Enter Values only, no evaluation if entered values
#	is correct or not.
#
# Rev2: Print the hypotenuse by changing it to str then using
#	using the concatenation string operatore (+) 

legA=float(input("Enter Leg A length: "))
legB=float(input("Enter Leg B length: "))

hypo=round((legA**2+legB**2)**0.5,2)

print("Hypotenuse is equal to "+str(hypo))
