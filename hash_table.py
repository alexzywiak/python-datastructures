#!/usr/bin/env python -tt

import string
import random

class HashTable():
  
  def __init__(self):
    self.limit = 8
    self.storage = [None] * self.limit
    self.item_count = 0
    self.resizing = False

  def get_index(self, k):
    return hash(k) % self.limit

  def insert(self, k, v):
    idx = self.get_index(k)
    if self.storage[idx]:
      updated = False
      for pair in self.storage[idx]:
        if pair[0] == k:
          pair[1] = v
          updated = True
      if not updated:
        self.storage[idx].append([k, v])
    else:
      self.storage[idx] = [[k, v]]

    self.check_resize(1)

  def retrieve(self, k):
    idx = self.get_index(k)

    if self.storage[idx]:
      for pair in self.storage[idx]:
        if pair[0] == k:
          return pair[1]
    return None

  def remove(self, k):
    idx = self.get_index(k)
    if self.storage[idx]:
      for pair in self.storage[idx]:
        if pair[0] == k:
          self.check_resize(-1)
          value = pair[1]
          self.storage[idx].remove(pair)
          return value
    return None

  def check_resize(self, change):
    self.item_count += change

    if not self.resizing:
      if self.item_count / float(self.limit) > 0.75:
        self.resize(self.limit * 2)
      if self.item_count / float(self.limit) < 0.25 and self.limit > 8:
        self.resize(self.limit / 2)


  def resize(self, new_limit):

    old_storage = self.storage
    self.limit = new_limit
    self.storage = [None] * self.limit
    self.item_count = 0

    self.resizing = True

    for bucket in old_storage:
      if bucket:
        for pair in bucket:
          if pair:
            self.insert(pair[0], pair[1])

    self.resizing = False

def test_hash_table():

  ht = HashTable()
  
  if not isinstance(ht, HashTable):
    print 'FAIL: hash table should an instance of HashTable'
    return

  if not type(ht.get_index('key')) is int:
    print 'FAIL: key should be an int'
    return

  for i in range(0, 1000):
    key = random_key_gen()
    idx = ht.get_index(key)
    if idx > ht.limit or idx < 0:
      print 'FAIL: hash index is out of bounds'
      return

  if not ht.get_index('key') == ht.get_index('key'):
    print 'FAIL:  should return same index for same key'
    return

  ht.insert('a', 1)
  ht.insert('b', 2)

  if not len(ht.storage):
    print 'FAIL:  should insert values into storage'
    return 

  if not ht.retrieve('a') == 1:
    print 'FAIL:  should retrieve values for existing keys'
    return 

  if ht.retrieve('z'):
    print 'FAIL:  should not retrieve values for non existant keys'
    return

  ht.insert('a', 2)

  if not ht.retrieve('a') == 2:
    print 'FAIL:  should update existing keys'
    return  

  ht.remove('a')

  if ht.retrieve('a'):
    print 'FAIL:  should remove keys'
    return 

  for i in range(0, 8):
    ht.insert(str(i), i)

  if len(ht.storage) == 8:
    print 'FAIL: Should grow in size'
    return

  for i in range(0, 8):
    ht.remove(str(i))

  if len(ht.storage) == 16:
    print 'FAIL: Should shrink in size'
    return

  print "SUCCESS:  You did it bro!  You\'re the best dev ever!"

def random_key_gen():
  chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
  return ''.join(random.choice(chars) for i in range(10))

def main():
  test_hash_table()
if __name__ == "__main__":
  main()