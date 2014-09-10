from math import *
from lib import *

board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
addrandomnumber(board,n=2)
printboard(board)
#board has been initiated with two tiles
if (True):
	move = raw_input("Please choose where to go(\"w;a;s;d\"): ")
	if move == "d":
		print("dddddd")
		moveright()
	elif move == "s":
		movedown()
	elif move == "a":
		moveleft()
	elif move == "w":
		moveup()