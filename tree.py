#!/usr/bin/env python -tt

class Tree():
  def __init__(self, value=None):
    self.value = value
    self.children = []

  def add_child(self, value):
    leaf = Tree(value)
    self.children.append(leaf)

  def contains(self, value):
    if self.value == value:
      return True
    else:
      for child in self.children:
        if child.contains(value):
          return True
      return False

def test_tree():
  tree = Tree()

  assert isinstance(tree, Tree), 'Should be an instance of Tree'

  tree.add_child(1)
  tree.add_child(2)

  assert len(tree.children) == 2, 'Should add children'
  assert isinstance(tree.children[0], Tree), 'Should save child nodes as tree instances'

  tree.children[0].add_child(3)
  tree.children[0].children[0].add_child(4)

  assert tree.contains(1), 'Should find values of children'
  assert tree.contains(4), 'Should find values of nested children'
  assert tree.contains(12) == False, 'Should not find values that don\'t exist'


  print 'SUCCESS:  No one suspects the Spanish Inquisition!'

def main():
  test_tree()

if __name__ == "__main__":
  main()