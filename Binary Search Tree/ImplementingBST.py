class Node:
	def __init__(self,value = None):
		self.value = value
		self.left = None
		self.right = None

class binary_search:
	def __init__(self):
		self.root = None

	def insert(self,value):
		if self.root == None:
			self.root = Node(value)
		else:
			self._insert(value,self.root)

	def _insert(self,value,cur_node):
		if value < cur_node.value:
			if cur_node.left == None:
				cur_nod.left = Node(value)
			else:
				self._insert(value,cur_node.left)
		else: 
			if cur_node.right == None:
				cur_nod.right = Node(value)
			else:
				self._insert(value,cur_node.right)




			

