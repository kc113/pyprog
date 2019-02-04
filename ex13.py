from sys import argv
from os.path import exists

script,from_file,to_file = argv
#open input file
in_file = open(from_file)
#read the content to txt
txt = in_file.read()
print("The input file is %d bytes long." % len(txt))

print("Does the output file exists? %r" % exists(to_file))
input("?")
out_file = open(to_file,'w')
out_file.write(txt)
out_file.close()
in_file.close()
