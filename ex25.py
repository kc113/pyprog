import random
from urllib.request import urlopen
import sys

word_url = "http://learncodethehardway.org/words.txt"
words = []
pharse = {"class %%%(%%%)" : "Make a class named %%% that is-a %%%",
		"class %%%(object): \n\tdef __init__(self,***)" :
		"class %%% has-a __init__ that takes self and *** parameters.",
		"class %%%(object):\n\tdef ***(self,@@@)" :
		"class %%% has-a function named *** that takes self and @@@ parameters.",
		"*** = %%%()" :
		"set *** to an instance of class %%%",
		"***.***(@@@)" :
		"from *** get the *** function, call it with parameters self and @@@",
		"***.*** = '***'" :
		"From *** get the *** attribute and set it to '***'"
		}

phase_1 = False
if len(sys.argv) == 2 and sys.argv[1] == 'eng':
	phase_1 = True

for word in urlopen(word_url).readlines():
	words.append(word.strip().decode('utf-8'))
	
def convert(snippet,phrase):
	class_names = [w.capitalize() for w in random.sample(words,snippet.count("%%%"))]
	other_names = random.sample(words,snippet.count("***"))
	results = []
	param_names = []
	
	for i in range(0,snippet.count("@@@")):
		param_count = random.randint(1,3)
		param_names.append(', '.join(random.sample(words,param_count)))
		
	for sen in snippet, phrase:
		result = sen[:]
		
		for word1 in class_names:
			result = result.replace("%%%",word1,1)
		for word1 in other_names:
			result = result.replace("***",word1,1)	
		for word1 in param_names:
			result = result.replace("@@@",word1,1)
		results.append(result)
	return results
	
try:
	while True:
		snippets = list(pharse.keys())
		random.shuffle(snippets)
		for snippet in snippets:
			phrase1 = pharse[snippet]
			ques, ans = convert(snippet,phrase1)
			if phase_1:
				ques, ans = ans, ques
			print(ques)
			input(">")
			print("ANSWER = %s\n" % ans)
except EOFError:
	print("\nBye")


	
	