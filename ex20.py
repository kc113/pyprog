print("You enter a room with 2 doors. Do you go through door #1 or door #2")
door = int(input("<"))
if door == 1:
	print("There is a giant bear. what do you do?")
	print("1-Take the cake.")
	print("2-Scream")
	bear = int(input("<"))
	if(bear == 1):
		print("Bear eats your face")
	elif(bear == 2):
		print("Bear eats your leg")
	else:
		print("bear runs away")

elif door == 2: 
	print("There is a cat.")
else:
	print("you die!")

	