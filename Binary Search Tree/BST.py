class BinarySearchTree:

	def __init__(self):
		self.root = None
		self.size = 0

	def length(self):
		return self.size

	def _length(self):
		return self.size

	def __iter__(self):
		return self.root.__iter__()


	def insert(self,key,val):
		if self.root:
			self._insert(self.key,value,self.root)
		else:
			self.root = TreeNode(key,val)
		self.size = self.size + 1

	def _insert(self,key,value,cur_node):
		if key < cur_node.key:
			if cur_node.hasLeftChild():
				self._insert(key,value,cur_node.leftChild)
			else:
				cur_node.leftChild = TreeNode(key, val,parent = cur_node)



class TreeNode:
	def __init__(self,key,val,left = None,right =None,parent = None):
		self.key = key
		self.value = value
		self.left = left
		self.right = right
		self.parent = parent

	def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self
