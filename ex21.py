count = [1,2,3,4,5]
fruits = ["orange","pear","apricot"]
change = [1,"penny",2,"dimes"]

for no in count:
	print("This is count %d" % no)
	
for fruit in fruits:
	print("fruit %s" % fruit)
	
for i in change:
	print("I got %r" % i)
	
elements = []
for i in range(0,6):
	print("Adding %d to the list" % i)
	elements.append(i)
	
print(elements)