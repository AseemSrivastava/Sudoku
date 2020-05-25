import random
import pprint
import myChoice
import checkBox
import time
def create():	
	#matrix to store/display sudoku board values 
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

	countValues = [9,9,9,9,9,9,9,9,9]	#Stores number of values remaining which can be inserted (1-9) note: total 9 values can be inserted of each weight(1-9) 
	
	X_Cord = [9,9,9,9,9,9,9,9,9]  	#Stores number of empty cell present in each X-axis
	
	Y_Cord = [9,9,9,9,9,9,9,9,9]  	#Stores number of empty cell present in Y-axis
	
	X_Index = [0,1,2,3,4,5,6,7,8]	#Stores X coordinates to check if atleast anyone X coordinate is empty of corresponding value
	
	Y_Index = [0,1,2,3,4,5,6,7,8]	#Stores Y coordinates to check if atleast anyone Y coordinate is empty of corresponding value
	
	v = int(input("Enter number of known values to put in sudoku board ")) #Ask user to specify number of squares to fill in the suduko board (1-81) 
	
	if v < 0 or v > 81:		#Condition to check for wrong input, If yes execute infinite loop until user input correct value
	
		while True:		#Loop to check if input value is correct, if not ask for input again
			print("Value should be from 1 to 81 ")
	
			v = int(input("Enter number of known values to put in sudoku board ")) #Ask user to specify number of squares to fill in the suduko board (1-81)
	
			if v > 0 and v < 82:	#Condition to check for correct input, if yes break the loop
				break
	print("Press 1 to generate the board automatically")
	print("Press 2 to generate the board manually")
	
	ch = int(input())	#Ask user to specify if the board will be user generated(Manual) or PC generated(Auto)
	
	if ch < 1 or ch > 2:	#Condition to check for wrong input if yes, execute infinite loop until user input correct value
	
		while True:  #Loop to check if input value is correct, if not ask for input again
	
			print("Wrong Input... Please choose from given option only")
			print("Press 1 to generate the board automatically")
			print("Press 2 to generate the board manually")
	
			ch = int(input())	#Ask the user to specify if the board will be user generated(Manual) or PC generated(Auto)
	
			if ch == 1 or ch == 2:	#Condition to check for correct input, if yes break the loop
				break
	
	execution_time = time.time()	#Stores the time at which input work is finished
	count = 0
	while(count < v):	#Loop to check if required number of squares are filled or not as specified by user
		check = True
		while(True):	#Loop to select valid number and valid coordinates to fill in sudoku board
			
			if(ch == 1):	#Conditon to check id board is to be generated is auto or not
				x = random.choice(X_Index)
				y = random.choice(Y_Index)
				box = checkBox.check(x,y)	
				avail = countValues[box]	#Stores the value of availbale space to insert in box
											#1st column is box 0 where x = 0 to 2 and y = 0 to 2
											#2nd column is box 1 where x = 0 to 2 and y = 3 to 5
											#4th column is box 4 where x = 3 to 5 and y = 0 to 2... and so on
											#There are total 9 columns coulmn 0 to column 8
				
				while avail == 0:			#If space not available then run loop infinte until space is found	
					print("Box is full cannot insert... choosing another coordinates")
					x = random.choice(X_Index)
					y = random.choice(Y_Index)
					box = checkBox.check(x,y)
					avail = countValues[box]

				num = myChoice.take(box, num = None)	#Call myChoice module to take a random number to input in sudoku grid
				break

			elif(ch == 2):	#ondition to check if board is to be genrated is manual or not
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

		if board[x][y] == 0:	#Condition to check if selected coordinate has value already inserted or not
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


			if check == True:		#Condition to check if given value can be inserted or not at given coordinate
				board[x][y] = num 	#Insert Number
				count = count + 1	#Increment count value to specify number values inserted
				countValues[box] = countValues[box] - 1	#Reduce the avilable number to insert in box by one
				X_Cord[x] = X_Cord[x] - 1	#Reduce the available number to insert in given x-axis by one
				Y_Cord[y] = Y_Cord[y] - 1	#Reduce the available number to insert in given y-axis by one
				if X_Cord[x] == 0:	#Check if all values are inserted for given x coordinate
					X_Index.remove(x)	#Remove the given value for X coordinate if all values are filled
				if Y_Cord[y] == 0:	#Check if all vlaues are inseerted for given y coordinate
					Y_Index.remove(y)	#Remove the given value for Y coordinate if all values are filled
				print("Number inserted sucessfully")
				print("Current board is")
				pprint.pprint(board) 		#Print the Sudoku board
				print("##############################")
			else:
				print("Cannot insert number because same value is present at given row/column")
				myChoice.take(box, num)	#Call the myChoice module to insert the number back in file because number not inserted in sudoku board
		else:
			print("Some value already present at given coordinates...Cannot insert")
			myChoice.take(box, num)		#Call the myChoice module to insert the number back in file because number not inserted in sudoku board

	#Print total execution time(ignoring input time taken by user) and time taken by user to input values
	print("Total execution time after ignoring the input time of user is %s seconds " % (time.time() - execution_time))
	print("Time taken by user to input the data "+str(time.time() - start_time - (time.time() - execution_time)))

if __name__ == "__main__":	#Main to tell Python to start execution of program from here
	start_time = time.time() #Stores start time of program
	num = [1,2,3,4,5,6,7,8,9]	#Stores valid set of values to be inserted in board
	#Insert all valid values in 9 different files each for one grid
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

	
	create()	#Call create function 

	#Print total time taken by Program to execute
	print("Total execution time %s seconds " % (time.time() - start_time))
	