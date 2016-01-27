#!/usr/bin/env python -tt

class Graph():

  def __init__ (self):
    self.nodes = {}

  def add_node(self, value):
    if not value in self.nodes:
      self.nodes[value] = {}

  def contains(self, value):
    return value in self.nodes

  def remove_node(self, value):
    if value in self.nodes:
      del self.nodes[value]
      return value
    return False

  def add_edge(self, a, b):
    if a in self.nodes and b in self.nodes:
      self.nodes[a][b] = True
      self.nodes[b][a] = True

  def has_edge(self, a, b):
    return b in self.nodes[a]

  def remove_edge(self, a, b):
    del self.nodes[a][b]
    del self.nodes[b][a]
    return

  def for_each_node(self, func):
    for node in self.nodes:
      func(node)
    return


def test_graph():

  graph = Graph()

  if not graph:
    print 'FAIL: Graph is not an object'
    return

  graph.add_node('a')

  if not 'a' in graph.nodes:
    print 'FAIL: did not add node'
    return

  if not type(graph.nodes['a']) is dict:
    print 'FAIL: did not add "a" list for node'
    return

  if not graph.contains('a'):
    print 'FAIL: contains should return True for existing nodes'
    return

  if graph.contains('b'):
    print 'FAIL: contains should return False for non-existent nodes'
    return

  graph.remove_node('a')

  if graph.contains('a'):
    print 'FAIL: "a" should be removed'
    return

  graph.add_node('a')
  graph.add_node('b')
  graph.add_node('c')

  graph.add_edge('a', 'b')

  if not graph.has_edge('a', 'b'):
    print 'FAIL: add and find existing edges'
    return  

  if not graph.has_edge('b', 'a'):
    print 'FAIL: edges should be mutual'
    return  

  if graph.has_edge('a', 'c'):
    print 'FAIL: not find non existent edges'
    return

  graph.remove_edge('a', 'b')

  if graph.has_edge('a', 'b'):
    print 'FAIL: not find removed edges'
    return  

  def print_nodes(node):
    print node

  graph.for_each_node(print_nodes)

  print "SUCCESS:  You did it bro!"


def main():
  test_graph()


if __name__ == "__main__":
  main()