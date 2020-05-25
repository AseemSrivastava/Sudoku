import random
import pprint
import myChoice
import checkBox
import time
def create(countValues):	
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

	X_Cord = [9,9,9,9,9,9,9,9,9]
	Y_Cord = [9,9,9,9,9,9,9,9,9]
	X_Index = [0,1,2,3,4,5,6,7,8]
	Y_Index = [0,1,2,3,4,5,6,7,8]
	v = int(input("Enter number of known values to put in sudoku board "))
	if v < 0 or v > 81:
		while True:
			print("Value should be from 1 to 81 ")
			v = int(input("Enter number of known values to put in sudoku board "))
			if v > 0 and v < 82:
				break
	print("Press 1 to generate the board automatically")
	print("Press 2 to generate the board manually")
	ch = int(input())
	if ch < 1 or ch > 2:
		while True:
			print("Wrong Input... Please choose from given option only")
			print("Press 1 to generate the board automatically")
			print("Press 2 to generate the board manually")
			ch = int(input())
			if ch == 1 or ch == 2:
				break
	execution_time = time.time()
	count = 0
	while(count < v):
		check = True
		while(True):
			if(ch == 1):
				x = random.choice(X_Index)
				y = random.choice(Y_Index)
				box = checkBox.check(x,y)
				avail = countValues[box]
				#This while loop should not run since box is only selected if it has spaces left
				while avail == 0:
					print("Box is full cannot insert... choosing another coordinates")
					x = random.choice(X_Index)
					y = random.choice(Y_Index)
					box = checkBox.check(x,y)
					avail = countValues[box]

				num = myChoice.take(box, num = None)
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
			box = checkBox.check(x,y)

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
				countValues[box] = countValues[box] - 1
				X_Cord[x] = X_Cord[x] - 1
				Y_Cord[y] = Y_Cord[y] - 1
				if X_Cord[x] == 0:
					X_Index.remove(x)
				if Y_Cord[y] == 0:
					Y_Index.remove(y)
				print("Number inserted sucessfully")
				print("Current board is")
				pprint.pprint(board) 
				print("##############################")
			else:
				print("Number cannot insert since citeria do not match for valid board")
				myChoice.take(box, num)
		else:
			print("Some value already present at given coordinates...Cannot insert")
			myChoice.take(box, num)


	print("Total execution time after ignoring the input time of user is %s seconds " % (time.time() - execution_time))


if __name__ == "__main__":
	start_time = time.time()
	num = [1,2,3,4,5,6,7,8,9]
	with open('num0.txt', 'w') as file:
		for n in num:
			file.write("%i\n" % n)

	with open('num1.txt', 'w') as file:
		for n in num:
			file.write("%i\n" % n)
	
	with open('num2.txt', 'w') as file:
		for n in num:
			file.write("%i\n" % n)
	
	with open('num3.txt', 'w') as file:
		for n in num:
			file.write("%i\n" % n)

	with open('num4.txt', 'w') as file:
		for n in num:
			file.write("%i\n" % n)

	with open('num5.txt', 'w') as file:
		for n in num:
			file.write("%i\n" % n)

	with open('num6.txt', 'w') as file:
		for n in num:
			file.write("%i\n" % n)

	with open('num7.txt', 'w') as file:
		for n in num:
			file.write("%i\n" % n)

	with open('num8.txt', 'w') as file:
		for n in num:
			file.write("%i\n" % n)

	countValues = [9,9,9,9,9,9,9,9,9]

	create(countValues)
	print("Total execution time %s seconds " % (time.time() - start_time))
	