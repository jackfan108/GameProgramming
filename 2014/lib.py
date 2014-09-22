from sys import *
from random import *
from math import log

def printboard(board):
	for i in board:
		print("---------------------")
		stdout.write("|")
		for k in i:
			if k == 0:
				stdout.write("    |")
				continue
			if int(log(k)/log(10)) == 3:
				stdout.write(str(k))
			elif int(log(k)/log(10)) == 2:
				stdout.write(" " + str(k))
			elif int(log(k)/log(10)) == 1:
				stdout.write(" " + str(k) + " ")
			else:
				stdout.write("  " + str(k) + " ")
			stdout.write("|")
		stdout.write("\n")
	print("---------------------")

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
	return board


def moveleft(board):
	for i in range(4):
		for k in range(3):
			if board[i][k+1] == 0:
				
			if board[i][k+1] == board[i][k]:
				board[i][k] *= 2
				board[i][k+1] = 0


	stdout.write("left")
def moveright():
	print("abc")
	stdout.write("right")
def moveup():
	stdout.write("up")
def movedown():
	stdout.write("down")
