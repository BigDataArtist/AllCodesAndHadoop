import random

def drawBoard(board):

	print('   |   |')
	print(''+board[7]+'|'+board[8]+'|'+board[9])  
	print('-----------')
	print(' | |')	
	print(' ' + board[4]+'|'+board[5]+'|'+board[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[1]+'|'+board[2]+'|'+board[3])
	print('   |   |')
	print(' | |')

def inputPlayerLetter():

	letter = ' '
	while letter !='X' and letter !='O':
		print('Do you want your letter X or O')
		letter=input().upper()

		if letter =='X':
			return['X','O']
		else:
			return['O','X']	

def whoGoesFirst():
	if random.randint(0,1) == 0:
		return "computer"
	else:
		return " player"

def playAgain():
	
	print(' you want to play again ?(Yes or NO)')
	return input().lower().startswith('y')	

def makeMove(board,letter,move):
	board[move]=letter

def isWinner(bo, le):
	return((bo[7]==le and bo[8]==le and bo[9]==le) or (bo[4]==le and bo[5]==le and bo[6]==le) or (bo[1]==le and bo[2]==le and bo[3==le]) or
		(bo[7] == le and bo[4] == le and bo[1] == le) or (bo[8] == le and bo[5] == le and bo[2] == le) or (bo[9] == le and bo[6] == le and bo[3] == le) or
		 (bo[7] == le and bo[5] == le and bo[3] == le) or (bo[9] == le and bo[5] == le and bo[1] == le))

def getBoardCopy(board):

	dupeBord=[]

	for i in board:
		dupeBoard.append(i)

	return dupeBoard

def isSpaceFree(board,move):
	return board[move]==' '

def getPlayerMove(board):
	 move =''

	while move not in '1,2,3,4,5,6,7,8,9'.split() or not isSpaceFree(board,int(move))
	print(' what is your nect move (1 to 9)')
	move = input()
return int(move)	

def chooseRandomMoveFromList(board, Moveslist):

	possibleMoves =[]
	for i in Moveslist:
	 	if isSpaceFree(board,i):
	 		possibleMoves.append(i)


	if len(possibleMoves)!=0:
		return random.choice(possibleMoves)
	else:
		return None	











