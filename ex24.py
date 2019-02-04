class song(object):
	def __init__(self,lyrics):
		self.lyrics = lyrics
	def sing(self):
		for line in self.lyrics:
			print(line)
happybday = song(["Happy birthday","to everyone"])
poem = ["rainy day","cool day"]
rain = song(poem)
happybday.sing()
rain.sing()
