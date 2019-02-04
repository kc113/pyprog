from sys import argv
script,filename = argv
def print_all(f):
	print(f.read())
def rewind(f):
	f.seek(0)
def print_line(l_count,f):
	print(l_count,f.readline(),end = '')
file = open(filename)
print_all(file)
rewind(file)
print_line(1,file)
print_line(2,file)
