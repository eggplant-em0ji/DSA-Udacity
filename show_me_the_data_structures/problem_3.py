import sys

# A Node class storing Huffman Encoding nodes
class HuffmanNode():
    def __init__(self, value, letter, left = None, right = None):
        self.value = value
        self.letter = letter
        self.left = left
        self.right = right
        self.huffman_code = ""

# After implementing a working solution that uses a sorted list for a priority queue which takes O(nlog(n)) time, I copied the template code for a min heap implementation in Python 
# from https://www.geeksforgeeks.org/min-heap-in-python/ in order to test whether the code works in an O(log(n)) time priority queue. I had some initial difficulty implementing an optimal min-heap myself from scratch.
# Then I adjusted it to hold HuffmanNodes rather than integers and changed all the methods accordingly. Later I attempted to fully understand the code then rewrite it in my normal syntax.
# Their copyright states that:
# You are free to:
# Share — copy and redistribute the material in any medium or format
# Adapt — remix, transform, and build upon the material for any purpose.
# Under the following terms:
# Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
# https://www.geeksforgeeks.org/copyright-information/
# A MinHeap of HuffmanNode() requires O(1) to copy/lookup the min value of all the HuffmanNodes in the heap. On average it requires O(log(n)) time to remove the min node and update the heap or insert an element and update the heap
class MinHeap():
    def __init__(self, maxsize):
        self.size = 0
        self.maxsize = maxsize
        self.heap = [HuffmanNode(-1, "Initializing MinHeap nodes of value -1 to fill min heap: no letter")]*(self.maxsize + 1)
        # self.heap[0] is not used because child and parent nodes are calculated using list indicies starting from root node at index 1
        self.heap[0] = HuffmanNode(-sys.maxsize, "self.heap[0] not used. No Letter")
        self.index_of_head_or_temp_head = 1

    # O(1)
    def parent(self, index):
        return index // 2
    # O(1)
    def left_child(self, index):
        return 2 * index
    # O(1)
    def right_child(self, index):
        return 2 * index + 1
    # O(1)
    def is_leaf(self, index):
        return (index*2 > self.size)
    # O(1)
    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]
    
    # O(log(n)) on average and worst case; O(1) in best case when index node is already a leaf or when index node already satisfies min heap qualities
    def heapify(self, index):
        if not self.is_leaf(index):
            if (self.heap[index].value > self.heap[self.left_child(index)].value or self.heap[index].value > self.heap[self.right_child(index)].value):
                if self.heap[self.left_child(index)].value < self.heap[self.right_child(index)].value:
                    self.swap(index, self.left_child(index))
                    self.heapify(self.left_child(index))
                else:
                    self.swap(index, self.right_child(index))
                    self.heapify(self.right_child(index))

    # O(log(n)) on average and worst case; O(1) in best case
    def insert(self, node):
        if self.size >= self.maxsize:
            return
        self.size+= 1
        # Adds new node to the end of the min heap list then swaps with parents as necessary to maintain min heap qualities
        self.heap[self.size] = node
        current = self.size
        while self.heap[current].value < self.heap[self.parent(current)].value:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    # O(log(n)) on average and worst case; O(1) in best case
    def remove(self):
        popped = self.heap[self.index_of_head_or_temp_head]
        # Takes last leaf element of min heap, assigns to temporary head of min heap then swaps nodes with child nodes as necessary to preserve min heap qualities
        self.heap[self.index_of_head_or_temp_head] = self.heap[self.size]
        self.size -= 1
        self.heapify(self.index_of_head_or_temp_head)
        return popped
    
    # O(1) returns by reference the head or min value of the MinHeap
    def copy_head_of_min_heap(self):
        return(self.heap[1])

# O(n) for each unique letter in the original phrase since to build encoding dict we must traverse from the root node to the each leaf node which all contain a unique letter
def calculate_huffman_code(node, code=""):
    new_code = code + node.huffman_code
    if node.left:
        calculate_huffman_code(node.left, new_code)
    if node.right:
        calculate_huffman_code(node.right, new_code)
    if not node.left and not node.right:
        codes[node.letter] = new_code

# O(nlog(n)) total time. O(n) for n chars in data and O(log(n)) each time the MinHeap elements must be position swapped to maintap min heap conditions after removing or inserting elements
def huffman_encoding(data):
    if data == None or type(data) != str:
        raise TypeError("Data input is invalid. Data must be a string.")
    elif len(data) == 0:
        raise ValueError("Data provided is invalid because it's a string of zero length")
    frequency_of_letters = {}
    # O(n) because it loops through each char in data
    for char in data:
        if char not in frequency_of_letters:
            frequency_of_letters[char] = 1
        else:
            frequency_of_letters[char] += 1
    # O(n) to initialize MinHeap of maxsize = len(data) + 1
    nodes = MinHeap(len(data))
    # O(n) to insert all the initial Huffman Nodes
    for char in frequency_of_letters.keys():
        nodes.insert(HuffmanNode(frequency_of_letters[char], char, left = None, right = None))
    # O(n) to pop HuffmanNodes from MinHeap and combine into one HuffmanNode then insert result into MinHeap until only one HuffmanNode remains
    while nodes.size > 1:
        left = nodes.remove()
        right = nodes.remove()
        left.huffman_code = "0"
        right.huffman_code = "1"
        new_node = HuffmanNode(left.value + right.value, "No letter: node is a non-leaf huffman node", left, right)
        nodes.insert(new_node)
    # O(n) because each the Huffman code for each char in original phrase must be calculated by traversing the MinHeap starting from head node to a the leaf node containing the char
    calculate_huffman_code(nodes.copy_head_of_min_heap())
    huffman_output = ""
    for char in data:
        huffman_output += codes[char]
    return huffman_output, nodes

# Recursive helper function for decoding Huffman encodings
# O(1) each time this helper function is called because it returns a decoded letter after processing a small finite number of 1s and 0s in the encoded data
def decode_message(data, node):
    if node.left == None and node.right == None:
        return node.letter, data 
    elif data[0] == "0":
        return(decode_message(data[1:], node.left))
    elif data[0] == "1":
        return(decode_message(data[1:], node.right))

# Function to decode an encoded message given the encoded data and the MinHeap tree of encodings
# O(n) to decode the original stentence because the recursive function must be called each time a char from the original phrase is decoded from the remaining 1s and 0s in the encoded data
def huffman_decoding(data,tree):
    decoded_message = ""
    top_node = tree.remove()
    while len(data) > 0:
        new_letter, data = decode_message(data, top_node)
        decoded_message += new_letter
    return(decoded_message)

if __name__ == "__main__":
    codes = {}

    a_great_phrase = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_phrase)))
    print ("The content of the data is: {}\n".format(a_great_phrase))

    encoded_data, tree = huffman_encoding(a_great_phrase)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1: Attempting to encode an integer
try:
    huffman_encoding(1)
except TypeError:
    print("Test Case 1: huffman_encoding(1) raises a TypeError because the input to huffman_encoding() is not a string\n")

# Test Case 2: Attempting to encode an empty string
try:
    huffman_encoding('')
except ValueError:
    print("Test Case 2: huffman_encoding('') raises a ValueError because the input to huffman_encoding() is a string of zero length\n")

# Test Case 3" Encoding a long JFK quote about going to the Moon
new_phrase = "We choose to go to the moon. We choose to go to the moon in this decade and do the other things, not because they are easy, "\
    "but because they are hard, because that goal will serve to organize and measure the best of our energies and skills, because that challenge "\
    "is one that we are willing to accept, one we are unwilling to postpone, and one which we intend to win, and the others, too."

print(f"Test Case 3: Encoding JFK quote: '{new_phrase}'\n")

encoded_data, tree = huffman_encoding(new_phrase)

print(f"Encoded data for JFK quote is '{encoded_data}'\n")

decoded_data = huffman_decoding(encoded_data, tree)

print(f"Decoded data for JFK quote is the original quote: '{decoded_data}'\n")

print(f"Test Case 3 Continued: Checking whether the the original phrase is the same as decoded data returns: {new_phrase == decoded_data}!.\n")

if new_phrase == decoded_data:
    print("Huffman Encoding algorithm successfully implemented in O(nlog(n)) time and Decoding algorithm in O(n) time! Ecoding takes O(nlog(n)) to process the encoded tree"\
        " for n unique letters in the original phrase. Decoding takes O(n) for n 1s or 0s in the encoded sequence.")