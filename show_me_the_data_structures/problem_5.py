import hashlib
from datetime import datetime
from time import sleep

# O(2511) for sha256() == O(1)
def calc_hash(hash_str):
      sha = hashlib.sha256()

      hash_str = hash_str.encode('utf-8')

      sha.update(hash_str)

      return sha.hexdigest()

class Block:
    def __init__(self, timestamp, data, previous_hash=None):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = calc_hash(data)
      self.next = None
      self.previous = None

class BlockChain():
    def __init__(self):
        self.head = None
        self.tail = None
    # O(1)
    def add_block(self, new_block):
        if self.head == None:
            self.head = new_block
            self.tail = self.head
        elif new_block.previous_hash != self.tail.hash:
            raise ValueError("Uh oh you attempted to add a block to a chain without the correct hash value of the last block in the blockchain!")
        else:
            new_block.previous = self.tail
            self.tail.next = new_block
            self.tail = new_block
    
    # Verifies that the blockchain you inherited is compliant with the properties of a blockchain
    # O(n) on n number of blocks in blockchain
    def verify_blockchain_integrity(self):
        curr_block = self.tail
        while curr_block.previous:
            if curr_block.previous_hash != curr_block.previous.hash:
                print("Blockchain integrity compromised!")
                return(False)
            curr_block = curr_block.previous
        return(True)


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1: Test basic implementation of BlockChain
print("Test Case 1: This test should print the data and hash values of the 3 added blocks into a new blockchain\n")
my_blockchain = BlockChain()
my_blockchain.add_block(Block(datetime.utcnow(), "hello I'm the first block"))
sleep(0.1)
my_blockchain.add_block(Block(datetime.utcnow(), "hello I'm the second block", my_blockchain.tail.hash))
sleep(0.1)
my_blockchain.add_block(Block(datetime.utcnow(), "hello I'm the third block", my_blockchain.tail.hash))
print(my_blockchain.head.data, "and my hash value is", my_blockchain.head.hash)
print(my_blockchain.head.next.data, "and my hash value is", my_blockchain.head.next.hash)
print(my_blockchain.tail.data, "and my hash value is ", my_blockchain.tail.hash)
print()

# Test Case 2: Verifying chain integrity
print(f"Test Case 2: The current blockchain's integrity check returns {my_blockchain.verify_blockchain_integrity()}!\n")

# Test Case 3: Attempting to add a block without valid parameters
try:
    my_blockchain.add_block()
except TypeError:
    print("Test Case 3: Attempting to add a block without a timestamp and string of data as the first two positional arguments results in a TypeError.\n")

# Test Case 4: Attempting to add a block without the previous block's hash value
try:
    my_blockchain.add_block(Block(datetime.utcnow(), "hello I'm the first block"))
except ValueError:
    print("Test Case 4: Attempting to add a block without the previous block's hash value results in a ValueError unless the blockchain is empty.\n")