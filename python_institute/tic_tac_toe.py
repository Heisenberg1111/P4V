#!/usr/bin/python3

#------------------------------------------
#
# Creates a Tic Tac Toe game using python
#
# 1 Player vs Computer
#
# Must be able to determine the winner
#
#------------------------------------------

# Draws the Tic Tac Toe board

def drawBoard(brdList):
	for rowVal in brdList:
		print("+ - - - + - - - + - - - +")
		print("|       |       |       |")
		print("|   "+ str(rowVal[0])+"   |   "+str(rowVal[1])+"   |   "+str(rowVal[2])+"   |")
		print("|       |       |       |")
	print("+ - - - + - - - + - - - +")

# Determine if the move is legit and available
def moveEval(num_move,uSER):
	global brdDict
	if num_move in brdDict:
		coord=brdDict[num_move]
		updateBoard(coord,uSER)
		del brdDict[num_move]
		return 1
	else:
		print(uSER,": Invalid Move. Move Again")
		return 0

def updateBoard(coord,uSER):
	global brd
	a,b=coord
	if uSER=="HUMAN":
		brd[a][b]="O"
	elif uSER=="COMP":
		brd[a][b]="X"
	else:
		print("User does not Exist")

# Computer Simulated Move
def compMove():
	from random import randrange
	
	if len(brdDict.keys())==0:
		return

	nice_move=0
	while nice_move==0:
		comp_move=randrange(8)+1
		nice_move=moveEval(comp_move,"COMP")
	
def checkBoard(uSER):
	
	if uSER=="HUMAN":
		piece="O"
	elif uSER=="COMP":
		piece="X"
	else:
		print("")

	for a in brd:
		if a[0]==piece and a[1]==piece and a[2]==piece:
			print(uSER,"WON!\n")
			return 1
	for i in range(3):
		if brd[0][i]==piece and brd[1][i]==piece and brd[2][i]==piece:
			print(uSER,"WON!\n")
			return 1

	if brd[0][0]==piece and brd[1][1]==piece and brd[2][2]==piece:
		print(uSER,"WON!\n")
		return 1
	elif brd[2][0]==piece and brd[1][1]==piece and brd[0][2]==piece:
		print(uSER,"WON!\n")
		return 1
	else:
		return 0
		



brd=[[1,2,3],[4,5,6],[7,8,9]]
brdDict={1:(0,0),2:(0,1),3:(0,2),4:(1,0),5:(1,1),6:(1,2),7:(2,0),8:(2,1),9:(2,2)}
drawBoard(brd)

while True:
	if len(brdDict.keys())==0:
		# Add Code for final board check
		print("\nGame End\n")
		break
	else:
		good_move=0
		while good_move==0:
			user_move=int(input("Enter Block Number to Move: "))
			good_move=moveEval(user_move,"HUMAN")
		drawBoard(brd)

		win=checkBoard("HUMAN")
		if win==1:
			break

		compMove()
		drawBoard(brd)

		win=checkBoard("COMP")
		if win==1:
			break
