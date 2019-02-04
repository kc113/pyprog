def break_words(stuff):
	words = stuff.split(" ")
	return words
	
def sort_word(words):
	return sorted(words)
	
def print_1st(words):
	word = words.pop(0)
	print(word)
	
def print_last(words):
	word = words.pop(-1)
	print(word)
	
def sort_sen(sen):
	words = break_words(sen)
	return sort_word(words)
	
def print_1st_last(sen):
	words = break_words(sen)
	print_1st(words)
	print_last(words)
	
def print_1st_last_s(sen):
	"""documentation"""
	words = sort_sen(sen)
	print_1st(words)
	print_last(words)