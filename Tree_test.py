class Node(object):

	def __init__(self, payload):
		self.payload = payload
		self.left = None
		self.right = None

	def insertPayload(self, payload):  # self is the current instance, or in our case current node
		if(self.payload):  # payload is the value passed to it.
			if(payload < self.payload):
				if(self.left):
					self.left.insertPayload(payload)
				else:
					self.left = Node(payload)
			elif(payload > self.payload):
				if(self.right):
					self.right.insertPayload(payload)
				else:
					self.right = Node(payload)
		else:
			self.payload = payload


# root -> left -> right
	def preorderTraversal(self):
		print(self.payload,end='->')
		if(self.left):
			self.left.preorderTraversal()
		if(self.right):
			self.right.preorderTraversal()
# left-> Root -> Right
	def inorderTraversal(self):
		if(self.left):
			self.left.inorderTraversal()
		print(self.payload,end='->')
		if(self.right):
			self.right.inorderTraversal()
# left -> right -> root
	def postorderTraversal(self):
		if(self.left):
			self.left.postorderTraversal()
		if(self.right):
			self.right.postorderTraversal()
		print(self.payload,end='->')
		

""" 	 1
	   /   \
	  2	    3
	 / \   / \
	4	5 6	  7

"""
"""
tree = Node(1)
tree.left = Node(2)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right = Node(3)
tree.right.left = Node(6)
tree.right.right = Node(7)

tree.preorderTraversal()
print('preorderTraversal')
tree.inorderTraversal()
print('inorderTraversal')
tree.postorderTraversal()
print('postorderTraversal')
"""
