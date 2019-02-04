people = 20
cat = 30
dog = 15

if people < cat:
	print("too many cats!")
if people > cat:
	print("too many people!")
if people > dog:
	print("more people than dogs!")
if people < dog:
	print("too many dogs!")
	
dog += 5
if people >= dog:
	print("more people than dogs!")
if people <= dog:
	print("too many dogs!")
if people == dog:
	print("people are dogs!")