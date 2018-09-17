# Please see instructions.pdf for the description of this problem.
from fixed_size_array import FixedSizeArray
from cs5112_hash import cs5112_hash1

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
    self.total_item_count = 0 # includes cells that have been flagged for removal

  # Inserts the `(key, value)` pair into the hash table, overwriting any value
  # previously associated with `key`.
  # Note: Neither `key` nor `value` may be None (an exception will be raised)
  def insert(self, key, value):
    if key is None or value is None:
      raise Exception("key, value cannot be None")

    h = cs5112_hash1(key) % self.array_size
    in_arr = self.get(key) is not None
    if not in_arr:
      self.item_count += 1
      self.total_item_count += 1
    ind = self._find_usable_index(key, h, in_arr)
    self.array.set(ind, (key, value, True))

    if self._get_current_load() > self.load_factor:
      self._resize_array()

  # Returns the value associated with `key` in the hash table, or None if no
  # such value is found.
  # Note: `key` may not be None (an exception will be raised)
  def get(self, key):
    if key is None:
      raise Exception("Key cannot be None")

    h = cs5112_hash1(key) % self.array_size
    for i in xrange(self.array_size):
      index = (h + i) % self.array_size

      # if we run into None, it isn't in the array
      if self.array.get(index) is None:
        return None
      # found it
      k,v,in_use = self.array.get(index)
      if k is key and in_use:
        return v
    return None

  # Removes the `(key, value)` pair matching the given `key` from the map, if it
  # exists. If such a pair exists in the map, the return value will be the value
  # that was removed. If no such value exists, the method will return None.
  # Note: `key` may not be None (an exception will be raised)
  def remove(self, key):
    if key is None:
      raise Exception("Key cannot be None")

    h = cs5112_hash1(key) % self.array_size
    for i in xrange(self.array_size):
      index = (h + i) % self.array_size

      # if we run into None, it isn't in the array
      if self.array.get(index) is None:
        return None

      # if we found it and it's in use, remove it
      k,v,in_use = self.array.get(index)
      if k is key and in_use:
        self.array.set(index, (k,v,False))
        self.item_count -= 1
        return v
    return None

  # Returns the number of elements in the hash table.
  def size(self):
    return self.item_count

  # Internal helper function for resizing the hash table's array once the ratio
  # of stored mappings to array size exceeds the specified load factor.
  def _resize_array(self):
    self.array_size *= 2
    self.item_count = 0
    self.total_item_count = 0
    prev_arr = self.array
    self.array = FixedSizeArray(self.array_size)
    for i in xrange(self.array_size / 2):
      if prev_arr.get(i) is None:
        continue
      k,v,in_use = prev_arr.get(i)
      if in_use:
        self.insert(k, v)

  # Internal helper function for accessing the array underlying the hash table.
  def _get_array(self):
    # DO NOT EDIT THIS METHOD
    return self.array

  def _get_current_load(self):
    return float(self.total_item_count) / self.array_size

  # finds the index that can be used to insert an element in the array
  def _find_usable_index(self, key, start_index, in_array):
    # potentially iterate over entire array
    for i in xrange(self.array_size):
      ind = (start_index + i) % self.array_size
      # if we find an empty cell, we know we can use it (and in_array must be False)
      if self.array.get(ind) is None:
        return ind

      k,_,in_use = self.array.get(ind)
      if not in_array:
        # we've found a cell that isn't empty but also isn't being used
        if not in_use:
          self.total_item_count -= 1 # we added to total item count assuming we weren't overwriting a value
          return ind
      else:
        # we've found the original cell
        if key is k:
          return ind
    return -1
