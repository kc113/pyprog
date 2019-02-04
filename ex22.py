from sys import exit
def gold_room():
	print("How much gold you want?")
	
	next = input("<")
	if "0" in next or "1" in next:
		quant = int(next)
	else:
		dead("Man, learn to type a no.")
	if quant < 50:
		print("You're not greedy, you win!")
		exit(0)
	else:
		dead("You're too greedy!")
	
def bear_room():
	bear_moved = False
	while True:
		next = input("<")
		if next == "take honey":
			dead("bear slaps.")
		elif next == "taunt bear" and not bear_moved:
			print("You can go.")
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("the bear chews your leg.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print("no idea what's going on.")

def cthulhu_room():
	next = input("<")
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Tasty!")
	else:
		cthulhu_room()

def dead(why):
	print(why,"good job!")
	exit(0)
	
def start():
	next = input("l or r")
	if next == 'l':
		bear_room()
	elif next == 'r':
		cthulhu_room()
	else:
		dead("You die")
start()
		

		
	
		