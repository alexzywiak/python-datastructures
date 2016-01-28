#!/usr/bin/env python -tt

class Node():
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList():

  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    
    node = Node(value)

    if not self.head:
      self.head = node
      self.tail = node
    else:
      self.tail.next = node
      self.tail = node

  def remove_head(self):
    if self.head:
      if self.head.next:
        self.head = self.head.next
      else:
        self.head = None

  def contains(self, value):
    node = self.head
    while node:
      if node.value == value:
        return True
      else:
        node = node.next
    return False


def linked_list_test():

  linked_list = LinkedList()

  assert isinstance(linked_list, LinkedList), 'Should be instance of linked list'

  linked_list.add_to_tail(1)

  assert isinstance(linked_list.head, Node), 'Should have a node instance at head'
  assert isinstance(linked_list.tail, Node), 'Should have a node instance at tail'
  assert linked_list.head.value == 1, 'Should hold value'

  linked_list.remove_head()
  assert linked_list.head == None, 'Should remove head if no other nodes exist'

  linked_list.add_to_tail(1)
  linked_list.add_to_tail(2)
  linked_list.remove_head()
  assert linked_list.head.value == 2, 'Should set new head object to next item in list'

  linked_list.add_to_tail(3)
  linked_list.add_to_tail(4)
  linked_list.add_to_tail(5)
  assert linked_list.contains(3), 'Should return true for existing values'
  assert linked_list.contains(12) == False, 'Should return false for non existant values'



  print 'SUCCESS:  You are the greatest pythoner ever!'


def main():
  linked_list_test()

if __name__ == "__main__":
  main()