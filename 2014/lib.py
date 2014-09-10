from sys import *
from random import *

def printboard(board):
	for i in board:
		print("--------------------------")
		stdout.write("|")
		for k in i:
			if k >= 0:
				stdout.write("  " + str(k) + "  " + "|")
		stdout.write("\n")
	print("--------------------------")

def addrandomnumber(board,n = 1):
	for i in range(n):
		#stdout.write("n = ")
		#print(n)
		flag = 0
		while(flag == 0):
			x = randint(0,3)
			#print(x)
			y = randint(0,3)
			#print(y)
			#print("board[x][y] = "+ str(board[x][y]))
			if board[x][y]==0:
				board[x][y] = 2 * randint(1,2)
				flag = 1
				#print("flag = " + str(flag))


def moveleft():
	stdout.write("left")
def moveright():
	print("abc")
	stdout.write("right")
def moveup():
	stdout.write("up")
def movedown():
	stdout.write("down")
