#import module
from sys import argv
#unpack argv
script, user_name = argv
prompt = '>>'

#get input and print.
print("Hi %s, I'm the %s script." % (user_name,script))
print("Do you like me %s?" % user_name)
likes = input(prompt)
print("where do you live %s" % user_name)
lives = input(prompt)
print("""
You said %r about liking me.
You live at %r.
"""% (likes,lives))

