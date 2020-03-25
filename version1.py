import numpy as np

boardState = ["E" for i in range(9)]

def stupidComputer(boardState):
	randomMove = np.random.randint(9)
	if (0 <= randomMove < 9 and boardState[randomMove] == "E"):
		boardState[randomMove] = "O"
		return 
	else:
		randomMove = np.random.randint(9)
		stupidComputer(boardState)

def smartComputer(boardState):
	# check for moves that can win the game
	for i in range(3):
		if (boardState[i] == boardState[i + 3] == "O"):
			if (boardState[i + 6] == "E"):
				boardState[i + 6] = "O"
				return
		elif (boardState[i + 3] == boardState[i + 6] == "O"):
			if (boardState[i] == "E"):
				boardState[i] = "O"
				return
		elif (boardState[i] == boardState[i + 6] == "O"):
			if (boardState[i + 3] == "E"):
				boardState[i + 3] = "O"
				return
		elif (boardState[i * 3] == boardState[i * 3 + 1] == "O"):
			if (boardState[i * 3 + 2] == "E"):
				boardState[i * 3 + 2] = "O"
				return 
		elif (boardState[i * 3 + 1] == boardState[i * 3 + 2] == "O"):
			if (boardState[i * 3] == "E"):
				boardState[i * 3] = "O"
				return 
		elif (boardState[i * 3] == boardState[i * 3 + 2] == "O"):
			if (boardState[i * 3 + 1] == "E"):
				boardState[i * 3 + 1] = "O"
				return 
	if (boardState[0] == boardState[4] == "O"):
		if (boardState[8] == "E"):
			boardState[8] = "O"
			return
	elif (boardState[0] == boardState[8] == "O"):
		if (boardState[4] == "E"):
			boardState[4] = "O"
			return
	elif (boardState[4] == boardState[8] == "O"):
		if (boardState[0] == "E"):
			boardState[0] = "O"
			return
	elif (boardState[2] == boardState[4] == "O"):
		if (boardState[6] == "E"):
			boardState[6] = "O"
			return
	elif (boardState[2] == boardState[6] == "O"):
		if (boardState[4] == "E"):
			boardState[4] = "O"
			return
	elif (boardState[6] == boardState[4] == "O"):
		if (boardState[2] == "E"):
			boardState[2] = "O"
			return

	# checking for moves that can lose the game
	for i in range(3):
		if (boardState[i] == boardState[i + 3] == "X"):
			if (boardState[i + 6] == "E"):
				boardState[i + 6] = "O"
				return
		elif (boardState[i + 3] == boardState[i + 6] == "X"):
			if (boardState[i] == "E"):
				boardState[i] = "O"
				return
		elif (boardState[i] == boardState[i + 6] == "X"):
			if (boardState[i + 3] == "E"):
				boardState[i + 3] = "O"
				return
		elif (boardState[i * 3] == boardState[i * 3 + 1] == "X"):
			if (boardState[i * 3 + 2] == "E"):
				boardState[i * 3 + 2] = "O"
				return 
		elif (boardState[i * 3 + 1] == boardState[i * 3 + 2] == "X"):
			if (boardState[i * 3] == "E"):
				boardState[i * 3] = "O"
				return 
		elif (boardState[i * 3] == boardState[i * 3 + 2] == "X"):
			if (boardState[i * 3 + 1] == "E"):
				boardState[i * 3 + 1] = "O"
				return 

	if (boardState[0] == boardState[4] == "X"):
		if (boardState[8] == "E"):
			boardState[8] = "O"
			return
	elif (boardState[0] == boardState[8] == "X"):
		if (boardState[4] == "E"):
			boardState[4] = "O"
			return
	elif (boardState[4] == boardState[8] == "X"):
		if (boardState[0] == "E"):
			boardState[0] = "O"
			return
	elif (boardState[2] == boardState[4] == "X"):
		if (boardState[6] == "E"):
			boardState[6] = "O"
			return
	elif (boardState[2] == boardState[6] == "X"):
		if (boardState[4] == "E"):
			boardState[4] = "O"
			return
	elif (boardState[6] == boardState[4] == "X"):
		if (boardState[2] == "E"):
			boardState[2] = "O"
			return
	#check corners: 0, 2, 6, 8
	for i in range(9):
		if (boardState[i] == "E" and i % 2 == 0 and i != 4):
			boardState[i] = "O"
			return

	#check center
	if (boardState[4] == "E"):
		boardState[4] = "O"
		return

	#if all else fails, place it on the sides: 1, 3, 5, 7
	for i in range(9):
		if (boardState[i] == "E" and i % 2 == 1):
			boardState[i] = "O"
			return

def printBoard(boardState):
		print(boardState[0:3])
		print(boardState[3:6])
		print(boardState[6:9])

def play(boardState):
	print("Input the number (1-9) you would like to place your X.")
	printBoard(boardState)
	number = int(input()) - 1
	if (0 <= number < 9 and boardState[number] == "E"):
		boardState[number] = "X"
	elif (number < 0 or number > 8):
		print("Your number is out of range. Please try again.")
		play(boardState)
	elif (boardState[number] != "E"):
		print("That square is already taken. Please try again")
		play(boardState)


	for i in range(3):
		if (boardState[i] == boardState[i + 3] == boardState[i + 6] == "X"):
			printBoard(boardState)
			print("You won!")
			exit()
		if(boardState[i * 3] == boardState[i * 3 + 1] == boardState[i * 3 + 2] == "X"):
			printBoard(boardState)
			print("You won!")
			exit()

	if (boardState[0] == boardState[4] == boardState[8]):
		if (boardState[0] == "X"):
			printBoard(boardState)
			print("You won!")
			exit()

	if (boardState[2] == boardState[4] == boardState[6]):
		if (boardState[2] == "X"):
			printBoard(boardState)
			print("You won!")
			exit()

	smartComputer(boardState)

	for i in range(3):
		if (boardState[i] == boardState[i + 3] == boardState[i + 6] == "O"):
			printBoard(boardState)
			print("You lost!")
			exit()
		if(boardState[i * 3] == boardState[i * 3 + 1] == boardState[i * 3 + 2] == "O"):
			printBoard(boardState)
			print("You lost!")
			exit()

	if (boardState[0] == boardState[4] == boardState[8]):
		if (boardState[0] == "O"):
			printBoard(boardState)
			print("You lost!")
			exit()

	if (boardState[2] == boardState[4] == boardState[6]):
		if (boardState[2] == "O"):
			printBoard(boardState)
			print("You lost!")
			exit()

	play(boardState)




print("Welcome to TikTacToe!")
play(boardState)


