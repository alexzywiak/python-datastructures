#!/usr/bin/env python -tt

class Stack():

	def __init__ (self):
		self._storage = {}
		self.top = 0

	def push(self, value):
		self._storage[self.top] = value
		self.top += 1

	def pop(self):
		if self.top >= 0:
			self.top -= 1
			value = self._storage[self.top]
			del self._storage[self.top]
			return value
		else:
			return None

	def size(self):
		return self.top


def test_stack():

	stack = Stack()

	stack.push('a')
	stack.push('b')
	stack.push('c')
	stack.push('d')

	if stack._storage[0] != 'a':
		print 'FAIL: Enstack blew it bro'
		return

	if stack._storage[1] != 'b':
		print 'FAIL: Enstack blew it bro'
		return

	if stack.size() != 4:
		print 'FAIL: Size blew it bro'
		return

	value = stack.pop()

	if value != 'd':
		print 'FAIL: Destack blew it bro'
		return

	if stack._storage.get(3, False):
		print 'FAIL: Destack blew it bro'
		return

	if stack.size() != 3:
		print 'FAIL: Size blew it bro'
		return

	print 'SUCCESS: stack works!'

def main():
	test_stack()

if __name__ == "__main__":
	main()