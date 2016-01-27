#!/usr/bin/env python -tt

class BinarySearchTree():

	def __init__ (self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, value):
		if value < self.value:
			if self.left:
				self.left.insert(value)
			else:
				self.left = BinarySearchTree(value)
		else:
			if self.right:
				self.right.insert(value)
			else:
				self.right = BinarySearchTree(value)


	def contains(self, value):
		
		if self.value == value:
			return True
		elif self.value > value:
			if self.left:
				return self.left.contains(value)
			else:
				return False
		else:
			if self.right:
				return self.right.contains(value)
			else:
				return False


	def depth_first_log(self, func):
		func(self)
		if self.left:
			self.left.depth_first_log(func)
		if self.right:
			self.right.depth_first_log(func)


def test_bst():
	bst = BinarySearchTree(5)

	if not bst:
		print 'FAIL: Constructor function does not exist'
		return

	if not hasattr(bst, 'left'):
		print 'FAIL: Should have a left prop'
		return

	if not hasattr(bst, 'right'):
		print 'FAIL: Should have a right prop'
		return

	if not hasattr(bst, 'insert'):
		print 'FAIL: Should have an insert method'
		return

	bst.insert(1)

	if bst.left.value != 1:
		print 'FAIL: Did not insert 1 properly'
		return

	if not hasattr(bst.left, 'insert'):
		print 'FAIL: It should insert a new instance of BST'
		return

	bst.insert(2)
	bst.insert(4)
	bst.insert(3)
	bst.insert(6)

	if not hasattr(bst, 'contains'):
		print 'FAIL: Should have a contains method'
		return

	if not bst.contains(2):
		print 'FAIL: Should find existing values'
		return

	if not bst.contains(4):
		print 'FAIL: Should find existing values'
		return

	if bst.contains(12):
		print 'FAIL: Should not find non-existing values'
		return

	def print_value(node):
		print node.value

	bst.depth_first_log(print_value)

	if not hasattr(bst, 'depth_first_log'):
		print 'FAIL: Should have a depth_first_log method'
		return

	print 'SUCCESS:  Everything works!  Great job dude!'


def main():
  test_bst()

if __name__ == "__main__":
	main()