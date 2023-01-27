class Node:
    def __init__(self, key, value):
        self._key = key
        self._value = value
        self._next = None
        self._prev = None

class OrderedDict():
    def __init__(self):
        self._start = None
        self._length = 0

    def get_value(self, key):
        if self._start is None:
            return(-1)
        else:
            n = self._start
            while n is not None:
                if n._key == key:
                    return(n._value)
                elif n._next == None:
                    return(-1)
                else:
                    n = n._next
    
    def is_key_in_cache(self, key):
        if self._start is None:
            return(False)
        else:
            n = self._start
            while n is not None:
                if n._key == key:
                    return(True)
                elif n._next == None:
                    return(False) 
                else:
                    n = n._next      

    def insert_at_end(self, key, value):
        if self._start is None:
            new_node = Node(key, value)
            self._start = new_node
            self._length = 1
            return
        n = self._start
        while n._next is not None:
            n = n._next
        new_node = Node(key, value)
        n._next = new_node
        new_node._prev = n
        self._length += 1

    def delete_at_start(self):
        if self._start is None:
            self._length = 0
            return 
        elif self._start._next is None:
            self._start = None
            self._length = 0
            return
        self._start = self._start._next
        self._start._prev = None
        self._length -= 1
    
    def move_to_end(self, key):
        if self._start is None:
            return
        else:
            n = self._start
            while n is not None:
                if n._key == key:
                    value = n._value
                    if n._prev == None:
                        self.delete_at_start()
                        self.insert_at_end(key, value)
                    elif n._next == None:
                        return
                    else:
                        prev = n._prev
                        next = n._next
                        prev._next = next
                        next._prev = prev
                        self._length -= 1
                        self.insert_at_end(key, value)
                n = n._next


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self._capacity = capacity
        self._cache = OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key == None:
            return(-1)
        elif self._cache.is_key_in_cache(key) == True:
            self._cache.move_to_end(key)
        return(self._cache.get_value(key))

    def set(self, key, value):
        if key == None:
            return
        elif self._cache.is_key_in_cache(key) == True:
            self._cache.move_to_end(key)
        elif self._cache._length >= self._capacity:
            self._cache.delete_at_start()
            self._cache.insert_at_end(key, value)
        else:
            self._cache.insert_at_end(key, value)
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(f"our_cache.get(1) returns {our_cache.get(1)} and should return 1") 
print(f"our_cache.get(2) returns {our_cache.get(2)} and should return 2")
print(f"our_cache.get(9) returns {our_cache.get(9)} and should return -1 because 9 is not present in the cache")
# our_cache.get(1)        # returns 1
# our_cache.get(2)       # returns 2
# our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(f"our_cache.get(3) returns {our_cache.get(3)} and should return -1 because the cache reached it's capacity and 3 was the least recently used entry")
# our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1: setting a None key
print(f"Test Case 1: our_cache.get(None) returns {our_cache.get(None)} and should return -1 because None is designed to be an invalid key\n")

# Test Case 2: setting a None value
our_cache.set(16, None)
print(f"Test Case 2: our_cache.get(16) returns {our_cache.get(16)} and should return None because the key 16 was set with a value of None\n")

# Test Case 3: attempting to set an empty key or value
try:
    our_cache.set(20)
except TypeError:
    print("Test Case 3: our_cache.set(20) results in a TypeError because we attempt to set a key-value pair without both the key and value\n")

# Test Case 4: large key value and strings
our_cache.set(1234567, "abcdef")
print(f"Test Case 4: our_cache.get(1234567) returns {our_cache.get(1234567)} and should return abcdef\n")