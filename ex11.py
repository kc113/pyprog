#import module
from sys import argv
#unpack argv
script,file_name = argv
#open the file.
text = open(file_name)
print(text)
#print the filename and content using command line.
print("Here is your filename %r:" % file_name)
print(text.read())
text.close()
#print file content using user input.
file_again = input("Type the file name")
txt = open(file_again)
print(txt)
print(txt.read())
txt.close()
