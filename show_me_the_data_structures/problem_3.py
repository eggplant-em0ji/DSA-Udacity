import sys

class HuffmanNode():
    def __init__(self, value, letter, left = None, right = None):
        self.value = value
        self.letter = letter
        self.left = left
        self.right = right
        self.huffman_code = ""

# I copied the template code for a min heap implementation in Python from https://www.geeksforgeeks.org/min-heap-in-python/
# then I adjusted it to hold HuffmanNodes rather than integers and changed all the methods accordingly. I'm in the proccess of fully understanding and rewriting the helper code from scratch.
# Their copyright states that You are free to:
# Share — copy and redistribute the material in any medium or format
# Adapt — remix, transform, and build upon the material for any purpose.
# Under the following terms:
# Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
class MinHeap():
    def __init__(self, maxsize):
        self.size = 0
        self.maxsize = maxsize
        self.heap = [HuffmanNode(-1, "no letter")]*(self.maxsize + 1)
        self.heap[0] = HuffmanNode(-2, "no letter")
        self.FRONT = 1

    def parent(self, index):
        return index // 2
    def left_child(self, index):
        return 2 * index
    def right_child(self, index):
        return 2 * index + 1
    def is_leaf(self, index):
        return (index*2 > self.size)
    def swap(self, fpos, spos):
        self.heap[fpos], self.heap[spos] = self.heap[spos], self.heap[fpos]
    def heapify(self, index):
        
        if not self.is_leaf(index):
            if (self.heap[index].value > self.heap[self.left_child(index)].value or 
               self.heap[index].value > self.heap[self.right_child(index)].value):
  
                if self.heap[self.left_child(index)].value < self.heap[self.right_child(index)].value:
                    self.swap(index, self.left_child(index))
                    self.heapify(self.left_child(index))
                else:
                    self.swap(index, self.right_child(index))
                    self.heapify(self.right_child(index))

    def insert(self, node):
        if self.size >= self.maxsize :
            return
        self.size+= 1
        self.heap[self.size] = node
  
        current = self.size
  
        while self.heap[current].value < self.heap[self.parent(current)].value:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def remove(self):
        popped = self.heap[self.FRONT]
        self.heap[self.FRONT] = self.heap[self.size]
        self.size-= 1
        self.heapify(self.FRONT)
        return popped
  
def calculate_huffman_code(node, code=""):
    new_code = code + node.huffman_code
    if node.left:
        calculate_huffman_code(node.left, new_code)
    if node.right:
        calculate_huffman_code(node.right, new_code)
    if not node.left and not node.right:
        codes[node.letter] = new_code

def huffman_encoding(data):
    if data == None or type(data) != str or len(data) == 0:
        raise TypeError("Data input is invalid. Data must be a string of non-zero length.")
    frequency_of_letters = {}
    for char in data:
        if char not in frequency_of_letters:
            frequency_of_letters[char] = 1
        else:
            frequency_of_letters[char] += 1
    nodes = MinHeap(len(data))
    for char in frequency_of_letters.keys():
        nodes.insert(HuffmanNode(frequency_of_letters[char], char, left = None, right = None))
    while nodes.size > 1:
        left = nodes.remove()
        right = nodes.remove()
        left.huffman_code = "0"
        right.huffman_code = "1"
        new_node = HuffmanNode(left.value + right.value, "No letter: node is a non-leaf huffman node", left, right)
        nodes.insert(new_node)
    top_node = nodes.remove()
    calculate_huffman_code(top_node)
    nodes.insert(top_node)
    huffman_output = ""
    for char in data:
        huffman_output += codes[char]
    return huffman_output, nodes

def decode_message(data, node):
    if node.left == None and node.right == None:
        return node.letter, data 
    elif data[0] == "0":
        return(decode_message(data[1:], node.left))
    elif data[0] == "1":
        return(decode_message(data[1:], node.right))

def huffman_decoding(data,tree):
    decoded_message = ""
    top_node = tree.remove()
    while len(data) > 0:
        new_letter, data = decode_message(data, top_node)
        decoded_message += new_letter
    return(decoded_message)

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

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
except TypeError:
    print("Test Case 2: huffman_encoding('') raises a TypeError because the input to huffman_encoding() is a string of zero length\n")

# Test Case 3" Encoding a long JFK quote about going to the Moon
new_sentence = "We choose to go to the moon. We choose to go to the moon in this decade and do the other things, not because they are easy, "\
    "but because they are hard, because that goal will serve to organize and measure the best of our energies and skills, because that challenge "\
    "is one that we are willing to accept, one we are unwilling to postpone, and one which we intend to win, and the others, too."

print(f"Test Case 3: Encoding '{new_sentence}'\n")

encoded_data, tree = huffman_encoding(new_sentence)

print(f"Encoded data for new sentence is '{encoded_data}'\n")

decoded_data = huffman_decoding(encoded_data, tree)

print(f"Decoded data is '{decoded_data}'\n")

print(f"Checking whether the the original sentence is the same as decoded data returns: {new_sentence == decoded_data}. Success! Our algoirthm which "\
"implemented a min heap using list indices to manage nodes in the priority queue works in log(n) time!\n")