#This Module is used to insert/delete value from files and return a random value from available values for particular grid 
import random
def take(box, num):
	temp = []
	if box == 0:
		with open('num0.txt', 'r') as file:
			for n in file:
				n = n.strip()
				temp.append(int(n))		
		if num is None:
			x = random.choice(temp)
			temp.remove(x)
			
			with open('num0.txt', 'w') as file:
				for n in temp:
					file.write("%i\n" % n)

			return x
		else:
			with open('num0.txt','a') as file:
				file.write(str(num))
			
			return

	elif box == 1:
		with open('num1.txt', 'r') as file:
			for n in file:
				n = n.strip()
				temp.append(int(n))		
		if num is None:
			x = random.choice(temp)
			temp.remove(x)
			
			with open('num1.txt', 'w') as file:
				for n in temp:
					file.write("%i\n" % n)

			return x
		else:
			with open('num1.txt','a') as file:
				file.write(str(num))
			
			return

	elif box == 2:
		with open('num2.txt', 'r') as file:
			for n in file:
				n = n.strip()
				temp.append(int(n))		
		if num is None:
			x = random.choice(temp)
			temp.remove(x)
			
			with open('num2.txt', 'w') as file:
				for n in temp:
					file.write("%i\n" % n)

			return x
		else:
			with open('num2.txt','a') as file:
				file.write(str(num))
			
			return

	elif box == 3:
		with open('num3.txt', 'r') as file:
			for n in file:
				n = n.strip()
				temp.append(int(n))		
		if num is None:
			x = random.choice(temp)
			temp.remove(x)
			
			with open('num3.txt', 'w') as file:
				for n in temp:
					file.write("%i\n" % n)

			return x
		else:
			with open('num3.txt','a') as file:
				file.write(str(num))
			
			return

	elif box == 4:
		with open('num4.txt', 'r') as file:
			for n in file:
				n = n.strip()
				temp.append(int(n))		
		if num is None:
			x = random.choice(temp)
			temp.remove(x)
			
			with open('num4.txt', 'w') as file:
				for n in temp:
					file.write("%i\n" % n)

			return x
		else:
			with open('num4.txt','a') as file:
				file.write(str(num))
			
			return

	elif box == 5:
		with open('num5.txt', 'r') as file:
			for n in file:
				n = n.strip()
				temp.append(int(n))		
		if num is None:
			x = random.choice(temp)
			temp.remove(x)
			
			with open('num5.txt', 'w') as file:
				for n in temp:
					file.write("%i\n" % n)

			return x
		else:
			with open('num5.txt','a') as file:
				file.write(str(num))
			
			return

	elif box == 6:
		with open('num6.txt', 'r') as file:
			for n in file:
				n = n.strip()
				temp.append(int(n))		
		if num is None:
			x = random.choice(temp)
			temp.remove(x)
			
			with open('num6.txt', 'w') as file:
				for n in temp:
					file.write("%i\n" % n)

			return x
		else:
			with open('num6.txt','a') as file:
				file.write(str(num))
			
			return

	elif box == 7:
		with open('num7.txt', 'r') as file:
			for n in file:
				n = n.strip()
				temp.append(int(n))		
		if num is None:
			x = random.choice(temp)
			temp.remove(x)
			
			with open('num7.txt', 'w') as file:
				for n in temp:
					file.write("%i\n" % n)

			return x
		else:
			with open('num7.txt','a') as file:
				file.write(str(num))
			
			return
	elif box == 8:
		with open('num8.txt', 'r') as file:
			for n in file:
				n = n.strip()
				temp.append(int(n))		
		if num is None:
			x = random.choice(temp)
			temp.remove(x)
			
			with open('num8.txt', 'w') as file:
				for n in temp:
					file.write("%i\n" % n)

			return x
		else:
			with open('num8.txt','a') as file:
				file.write(str(num))
			
			return


if __name__ == "__main__":
	pass
