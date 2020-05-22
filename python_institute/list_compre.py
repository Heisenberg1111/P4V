# List comprehension - Creating a list using an expression

squares = [ x**2 for x in range(10)] # square of numbers from 0 to 9

print("Squares:",squares)

odd=[x for x in squares if x%2!=0]

print("Odd Numbers from Squares", odd)
