def add(a,b):
	print("Adding %d + %d" % (a,b))
	return a + b

def sub(a,b):
	print("Subtracting %d - %d" % (a,b))
	return a - b
	
def mul(a,b):
	print("Multiplying %d * %d" % (a,b))
	return a * b
	
def div(a,b):
	print("Dividing %d / %d" % (a,b))
	return a / b
	
a1 = add(30,5)
a2 = sub(30,5)
a3 = mul(30,5)
a4 = div(30,5)

print("%d %d %d %d" % (a1,a2,a3,a4))
print(add(a1,sub(a2,mul(a3,div(a4,2)))))




