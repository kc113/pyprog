things = "Apple orange banana sugar light"
stuff = things.split(" ")
stuff_more = ["Day","night","song"]
while len(stuff_more) != 0:
	item = stuff_more.pop()
	print(item)
	stuff.append(item)
	
print(stuff)
print(stuff[1])
print(stuff[-1])
print(" ".join(stuff))
print("#".join(stuff[3:5]))
