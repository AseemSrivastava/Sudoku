#This Module is used to return the box number according to the given parameter

def check(x, y):
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

	return box



if __name__ == "__main__":
	pass