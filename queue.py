#!/usr/bin/env python -tt

class Queue():

	def __init__ (self):
		self._storage = {}
		self.enter = 0
		self.exit = 0

	def enqueue(self, value):
		self._storage[self.enter] = value
		self.enter += 1

	def dequeue(self):
		if self.enter > self.exit:
			value = self._storage[self.exit]
			del self._storage[self.exit]
			self.exit += 1
			return value
		else:
			return None

	def size(self):
		return self.enter - self.exit


def test_queue():

	queue = Queue()

	queue.enqueue('a')
	queue.enqueue('b')
	queue.enqueue('c')
	queue.enqueue('d')

	if queue._storage[0] != 'a':
		print 'FAIL: Enqueue blew it bro'
		return

	if queue._storage[1] != 'b':
		print 'FAIL: Enqueue blew it bro'
		return

	if queue.size() != 4:
		print 'FAIL: Size blew it bro'
		return

	value = queue.dequeue()

	if value != 'a':
		print 'FAIL: Dequeue blew it bro'
		return

	if queue._storage.get(0, False):
		print 'FAIL: Dequeue blew it bro'
		return

	if queue.size() != 3:
		print 'FAIL: Size blew it bro'
		return

	print 'SUCCESS: Queue works!'

def main():
	test_queue()

if __name__ == "__main__":
	main()