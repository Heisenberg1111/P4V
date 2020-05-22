secret_number=777

print(
"""
+=============================+
| Welcome to my game, muggle! |
| Enter an integer number     |
| and guess what number I've  |
| picked for you.             |
| So, what is the secret num? |
+=============================+
""")

number=int(input("Enter a Number: "))

while secret_number != number :
	print("\nHa ha! You're stuck in my loop\n")
	number=int(input("Enter a Number: "))

print("\nWell done, muggle! You are free now.")
