import numpy as np

boardState = ["E" for i in range(9)]



def smartComputer(boardState):
	# check for moves that can win the game
	for i in range(3):
		if (boardState[i] == boardState[i + 3] == "O"):
			if (boardState[i + 6] == "E"):
				return i + 6
		elif (boardState[i + 3] == boardState[i + 6] == "O"):
			if (boardState[i] == "E"):
				return i
		elif (boardState[i] == boardState[i + 6] == "O"):
			if (boardState[i + 3] == "E"):
				return i + 3
		elif (boardState[i * 3] == boardState[i * 3 + 1] == "O"):
			if (boardState[i * 3 + 2] == "E"):
				return i * 3 + 2
		elif (boardState[i * 3 + 1] == boardState[i * 3 + 2] == "O"):
			if (boardState[i * 3] == "E"):
				return i * 3 
		elif (boardState[i * 3] == boardState[i * 3 + 2] == "O"):
			if (boardState[i * 3 + 1] == "E"):
				return i * 3 + 1
	if (boardState[0] == boardState[4] == "O"):
		if (boardState[8] == "E"):
			return 8
	elif (boardState[0] == boardState[8] == "O"):
		if (boardState[4] == "E"):
			return 4
	elif (boardState[4] == boardState[8] == "O"):
		if (boardState[0] == "E"):
			return 0
	elif (boardState[2] == boardState[4] == "O"):
		if (boardState[6] == "E"):
			return 6
	elif (boardState[2] == boardState[6] == "O"):
		if (boardState[4] == "E"):
			return 4
	elif (boardState[6] == boardState[4] == "O"):
		if (boardState[2] == "E"):
			return 2

	# checking for moves that can lose the game
	for i in range(3):
		if (boardState[i] == boardState[i + 3] == "X"):
			if (boardState[i + 6] == "E"):
				return i + 6
		elif (boardState[i + 3] == boardState[i + 6] == "X"):
			if (boardState[i] == "E"):
				return i
		elif (boardState[i] == boardState[i + 6] == "X"):
			if (boardState[i + 3] == "E"):
				return i + 3
		elif (boardState[i * 3] == boardState[i * 3 + 1] == "X"):
			if (boardState[i * 3 + 2] == "E"):
				return  i * 3 + 2
		elif (boardState[i * 3 + 1] == boardState[i * 3 + 2] == "X"):
			if (boardState[i * 3] == "E"):
				return i * 3
		elif (boardState[i * 3] == boardState[i * 3 + 2] == "X"):
			if (boardState[i * 3 + 1] == "E"):
				return i * 3 + 1

	if (boardState[0] == boardState[4] == "X"):
		if (boardState[8] == "E"):
			return 8
	elif (boardState[0] == boardState[8] == "X"):
		if (boardState[4] == "E"):
			return 4
	elif (boardState[4] == boardState[8] == "X"):
		if (boardState[0] == "E"):
			return 0
	elif (boardState[2] == boardState[4] == "X"):
		if (boardState[6] == "E"):
			return 6
	elif (boardState[2] == boardState[6] == "X"):
		if (boardState[4] == "E"):
			return 4
	elif (boardState[6] == boardState[4] == "X"):
		if (boardState[2] == "E"):
			return 2
	#check corners: 0, 2, 6, 8
	for i in range(9):
		if (boardState[i] == "E" and i % 2 == 0 and i != 4):
			return i

	#check center
	if (boardState[4] == "E"):
		return 4

	#if all else fails, place it on the sides: 1, 3, 5, 7
	for i in range(9):
		if (boardState[i] == "E" and i % 2 == 1):
			return i

def printBoard(boardState):
		print(boardState[0:3])
		print(boardState[3:6])
		print(boardState[6:9])

