# Simple Program which will ask to Enter a Word
#
# Program will remove all vowels and spaces and recreate the word


userWord=input("Enter a Word: ")

userWord=userWord.upper()
newWord=""


for letter in userWord:

	if letter=="A" or letter=="E" or letter=="I" or letter =="O" or letter=="U" or letter==" ":
		continue
	else:
		print(letter)
		newWord=newWord+letter

print(newWord)
