def print_two(*args):
	arg1, arg2 = args
	print("%r %r" % (arg1,arg2))
	
def print_again2(arg1,arg2):
	print("%r %r" % (arg1,arg2))
	
def print_again1(arg1):
	print("%r" % (arg1))
	
def print_again0():
	print("print nothing")
	
print_two(1,2)
print_again2(6,7)
print_again1("keys")
print_again0()

	

