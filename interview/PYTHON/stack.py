# class stack:
# 	def __init__(self):
# 		self.l1 = [0]


# 	def push(self,item):

# 		s = self.l1.append(item)
# 		print(type(s),s)
# 	# def pop(self):
# 	# 	if len(self.stack) > 0:
# 	# 		return self.stack.pop()
# 	# 	else:
# 	# 		return self.stack

class Stack:
	def __init__(self):
		self.items = []
 
	def is_empty(self):
		return self.items == []
 
	def push(self, data):
		print(data)
		self.items.append(data)
		return self.items
 
	def pop(self):
		return self.items.pop()
 
 
s = Stack()

print(s.push(1))
