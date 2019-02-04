from sys import argv
#unpack argv
script, filename = argv

print("We're going to delete file %r" % filename)
print("press ctrl+c to undo")

input("?")
txt = open(filename,'w')
#trucate the file
txt.truncate()
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")
#write the lines in file.
txt.write(line1+"\n"+line2+"\n"+line3+"\n")
txt.close()