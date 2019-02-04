#stack ds using list
class Stack():
	#constructor to create a empty list.
	def __init__(self):
		self.stack = list()
	
	#check if stack is empty.
	def isEmpty(self):
		if len(self.stack) == 0:
			return True
		else:
			return False
			
	#adding element to list
	def push(self,data):
		self.stack.append(data)
		return True
		
	#deleting element from list
	def pop(self):
		if self.isEmpty() == False:
			return self.stack.pop()
		else:
			return "No element"
			

st = Stack()
print(st.isEmpty())
st.push(4)
st.push(5)
st.push(4)
print(st.pop())
print(st.stack)	
		
	
	