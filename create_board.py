import random
#import array as arr
import pprint
def create():	
	board = [
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,0,0,0]
		]
	v = int(input("Enter number of known values to put in sudoku board "))
	print("Press 1 for automatic generate")
	print("Press 2 for user generate")
	ch = int(input())
	count = 0
	while(count < v):
		check = True
		while(True):
			if(ch == 1):
				x = random.randint(0,8)
				y = random.randint(0,8)
				num = random.randint(1,9)
				break
			elif(ch == 2):
				x = int(input("Enter x coordinate to input value "))
				y = int(input("Enter y coordinate to input value "))
				num = int(input("Enter number to input "))
				if (x >= 0 and x <= 8) and (y >= 0 and y <= 8):
					if(num >= 1 and num <= 9):
						break	
					else:
						print("Number should be from 1 to 9 only ")
				else:
					print("x and y coordinates should be from 0 to 8 only ")
		if board[x][y] == 0:
			i = x
			for j in range(0,9):
				if board[i][j] == num:
					check = False
					break
			j = y
			for i in range(0,9):
				if board[i][j] == num:
					check = False
					break
			if x >= 0 and x <= 2 and y >= 0 and y <= 2:
				box = 0
		
			elif x >= 0 and x <= 2 and y >= 3 and y <= 5:
				box = 1
		
			elif x >= 0 and x <= 2 and y >= 6 and y <= 8:
				box = 2
		
			elif x >= 3 and x <= 5 and y >= 0 and y <= 2:
				box = 3
		
			elif x >= 3 and x <= 5 and y >= 3 and y <= 5:
				box = 4
		
			elif x >= 3 and x <= 5 and y >= 6 and y <= 8:
				box = 5
		
			elif x >= 6 and x <= 8 and y >= 0 and y <= 2:
				box = 6
		
			elif x >= 6 and x <= 8 and y >= 3 and y <= 5:
				box = 7
		
			elif x >= 6 and x <= 8 and y >= 6 and y <= 8:
				box = 8
		
			if box == 0:
				for i in range(0,3):
					for j in range(0,3):
						if board[i][j] == num:
							check = False
							break

			elif box == 1:
				for i in range(0,3):
					for j in  range(3,6):
						if board[i][j] == num:
							check = False
							break

			elif box == 2:
				for i in range(0,3):
					for j in  range(6,9):
						if board[i][j] == num:
							check = False
							break
			elif box == 3:
				for i in range(3,6):
					for j in  range(0,3):
						if board[i][j] == num:
							check = False
							break
			elif box == 4:
				for i in range(3,6):
					for j in  range(3,6):
						if board[i][j] == num:
							check = False
							break
			elif box == 5:
				for i in range(3,6):
					for j in  range(6,9):
						if board[i][j] == num:
							check = False
							break

			elif box == 6:
				for i in range(6,9):
					for j in  range(0,3):
						if board[i][j] == num:
							check = False
							break
			elif box == 7:
				for i in range(6,8):
					for j in  range(3,6):
						if board[i][j] == num:
							check = False
							break
			elif box == 8:
				for i in range(6,9):
					for j in  range(6,9):
						if board[i][j] == num:
							check = False
							break


			if check == True:
				board[x][y] = num
				count = count + 1
				print("Number inserted sucessfully")
				print("Current board is")
				pprint.pprint(board) 
				print("##############################")
		else:
			print("Some value already present at given coordinates...Cannot insert")

#pprint.pprint(board)
if __name__ == "__main__":
	create()
