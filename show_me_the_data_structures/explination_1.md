I decided to implement an OrderedDict to store the LRU Cache from scratch rather than use the built in one in Python.
I did not hash the key and hash table lookup method in this OrderedDict since the given maxsize of the cache in this problem was only 5. 
All operations in this implementation still approximately takes O(1) time since looking up a key in a hash table is not much faster than looping through 5 variables to check if a key matches.
Not hashing the key results in an O(5) for the get() and O(6) for set() methods in the worst case rather than O(1) and O(2) for using Python's built in OrderedDict respectively.
Removing the least recently used cache is still O(1) without a hash table since we are just removing the _start node in a doubly linked list.
The space complexity for the script is sys.getsizeof() of a filled LRU Cache, which is approximately O(1) for an LRU maxsize of 5.