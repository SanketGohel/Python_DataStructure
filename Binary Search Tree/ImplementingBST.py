class node:
	def __init__(self,value = None):
		self.value = value
		self.left = None
		self.right = None

class binary_search:
	def __init__(self):
		self.root = None

	def insert(self,value):
		if self.root == None:
			self.root = node(value)
		else:
			self._insert(value,self.root)

	def _insert(self,value,root):
		if value < root.value:
			if root.left == None:
				root.left = node(value)
			else:
				self._insert(value,root.left)
		else: 
			if root.right == None:
				root.right = node(value)
			else:
				self._insert(value,root.right)












			

