from math import *
from lib import *

board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
board = addrandomnumber(board,2)
board[1][2] = 16
board[2][3] = 128
board[0][1] = 1024
printboard(board)

#board has been initiated with two tiles
if (True):
	move = raw_input("Please choose where to go(\"w,a,s,d\"): ")
	if move == "d":
		print("dddddd")
		moveright(board)
	elif move == "s":
		movedown(board)
	elif move == "a":
		moveleft(board)
	elif move == "w":
		moveup(board)