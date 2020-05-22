# adding default values to function parameters


def intro(firstName, lastName="Smith"):
	print("Hello, my name is", firstName, lastName)



# supply both arguments

intro("Franlon","Asilo")

# supply only firstName


intro("Franlon")

intro(firstName="Sy")

# use keyword arguments

intro(lastName="Asilo",firstName="Franlon")
