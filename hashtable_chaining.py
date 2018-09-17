# Please see instructions.pdf for the description of this problem.
from fixed_size_array import FixedSizeArray
from cs5112_hash import cs5112_hash1

# Implementation of a node in a singlely linked list.
# DO NOT EDIT THIS CLASS
class SLLNode:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  def set_next(self, node):
    self.next_node = node

  def get_next(self):
    return self.next_node

  def set_value(self, value):
    self.value = value

  def get_value(self):
    return self.value

# An implementation of a hash table that uses chaining to handle collisions.
class HashTable:
  def __init__(self, initial_size=10, load_factor=.75):
    # DO NOT EDIT THIS CONSTRUCTOR
    if (initial_size < 0) or (load_factor <= 0) or (load_factor > 1):
      raise Exception("size must be greater than zero, and load factor must be between 0 and 1")
    self.array_size = initial_size
    self.load_factor = load_factor
    self.item_count = 0
    self.array = FixedSizeArray(initial_size)

  # Inserts the `(key, value)` pair into the hash table, overwriting any value
  # previously associated with `key`.
  # Note: Neither `key` nor `value` may be None (an exception will be raised)
  def insert(self, key, value):
    if key is None or value is None:
      raise Exception("key and value cannot be None")

    in_arr = self.get(key) is not None
    if not in_arr:
      self.item_count += 1

    ind = cs5112_hash1(key) % self.array_size
    cur_list = self.array.get(ind)
    if cur_list is None:
      self.array.set(ind, [(key, value)])
    else:
      # see if it's already in the list
      for i in xrange(len(cur_list)):
        k,_ = cur_list[i]
        if k is key:
          cur_list[i] = (key, value)
          return
      # it isn't already in the list
      cur_list.append((key, value))

    if self._get_current_load() > self.load_factor:
      self._resize_array()

  # Returns the value associated with `key` in the hash table, or None if no
  # such value is found.
  # Note: `key` may not be None (an exception will be raised)
  def get(self, key):
    if key is None:
      raise Exception("key cannot be None")

    ind = cs5112_hash1(key) % self.array_size
    cur_list = self.array.get(ind)
    # list doesn't exist, value must not be stored
    if cur_list is None:
      return None

    # search through list
    for k,v in cur_list:
      if k is key:
        return v
    # value was not found
    return None

  # Removes the `(key, value)` pair matching the given `key` from the map, if it
  # exists. If such a pair exists in the map, the return value will be the value
  # that was removed. If no such value exists, the method will return None.
  # Note: `key` may not be None (an exception will be raised)
  def remove(self, key):
    if key is None:
      raise Exception("Key cannot be None")

    ind = cs5112_hash1(key) % self.array_size
    cur_list = self.array.get(ind)
    ret_val = None

    # search through the list to see if the key is in it
    for i in xrange(len(cur_list)):
      if cur_list[i][0] is key: # found the key, so store the value
        ret_val = cur_list[i][1]
        self.item_count -= 1
        break

    # just create a new list and replace the old one
    new_list = [(k,v) for k,v in cur_list if k is not key]
    self.array.set(ind, new_list)
    return ret_val

  # Returns the number of elements in the hash table.
  def size(self):
    return self.item_count

  # Internal helper function for resizing the hash table's array once the ratio
  # of stored mappings to array size exceeds the specified load factor.
  def _resize_array(self):
    self.array_size *= 2
    self.item_count = 0
    prev_arr = self.array
    self.array = FixedSizeArray(self.array_size)

    for i in xrange(self.array_size / 2):
      if prev_arr.get(i) is None:
        continue

      cur_list = self.array.get(i)
      for k,v in cur_list:
        self.insert(k,v)

  # Internal helper function for accessing the array underlying the hash table.
  def _get_array(self):
    # DO NOT EDIT THIS FUNCTION
    return self.array

  def _get_current_load(self):
    return float(self.item_count) / self.array_size
