class node:
	def __init__(self, value = None):		
		self.value = value
		self.left_child = None
		self.right_child = None
		self.parent = None

class binary_search_tree:
	def __init__(self):
		self.root = None


	def insert(self,value):
		if self.root == None:
			self.root = node(value)
		else:
			self._insert(value,self.root)


	def _insert(self,value,cur_node):
		if value < cur_node.value:
			if cur_node.left_child = None:
				cur_node.left_child = node(value)
				cur_node.left_child.parent = cur_node
			else:
				self._insert(value,cur_node.left_child)
		elif value > cur_node.value:
			if cur_node.right_child = None:
				cur_node.right_child = node(value)
				cur_node.right_child.parent = cur_node
			else:
				self._insert(value,cur_node.right_child)
		else:
			print "Value already in tree!"


	# def height(self):
	# 	if self.root != None:
	# 		return self._height(self,root,0)
	# 	else
	# 		return 0

	# def _height(self,cur_node,cur_height):
	# 	if cur_node ==None:
	# 		return cur_height

	def search(self, value):
		if self.root !=	 None:
			return self._search(value,self.root)
		else:
			return False 

	def _search(self, value,cur_node):
		if value == cur_node.value:
			return True
		elif value < cur_node.value and cur_node.left_child != None:
			return self._search(value,cur_node.left_child)
		elif value > cur_node.value and cur_node.right_child != None:
			return self._search(value,cur_node.right_child)
		return False

	def find(self, value):
		if self.root != None:
			return self._find(value,self.root)
		else: 
			return None

	def _find(self,value,cur_node):
		if value == cur_node.value:
			return cur_node
		elif value < cur_node and cur_node.left_child != None:
			return self._find(value,cur_node.left_child)
		elif value > cur_node and cur_node.right_child != None:
			return self._find(value,cur_node.right_child)


	def delete_value(slef,value):
		return self.delete_node(self.find(value))

	def delete_node(self,node):

		def min_value_node(n):
			current = n 
			while current.left_child != None:
				current = current.left_child
			return current

		def num_children(n):
			num_children = 0
			if n.left_child!=None: num_children+=1
			if n.right_child!= None: num_children +=1 
			return num_children


		node_parent = node.parent

		#get the number of children of the node to be delete
		node_children = num_children(node)


		#break operation into different cases based on the struture of the tree and node to be delete

		#Case 1(node has no children):
		if node_children == 0:
			#remove reference to the node from the parent
			if node_parent.left_child == node:
				node_parent.left_child == None
			else:
				node_parent.right_child ==None

		#Case 2(node has single child)
		if node_children == 1:

			#get the single child node
			if node.left_child!=None:
				child = node.left_child
			else:
				child = node.right_child

			#replace the node to be deleted with its child
			if node_parent.left_child == node:
				node_parent.left_child = child
			else:
				node_parent.right_child = child

			#correct the parent pointer in node
			child.parent = node_parent


		#Case 3 (node has two children)
		if node_children == 2:

			#get the inorder successor of the deleted node
			successor = min_value_node(node.right_child)

			#copy the inorder successor's value to the node formerly holding the value we wished to delete
			node.value = successor.value
           
            # delete the inorder successor now that it's value was copied into the other node 
			self.delete_node(successor)





		






	def print_tree(self):
		if self.root != None:
			self._print_tree(self.root)


	def _print_tree(self,cur_node):
		if cur_node != None:
			self._print_tree(cur_node.left_child)
			print str(cur_node.value)
			self._print_tree(cur_node.right_child) 

















			

