import math

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

# Since a set() in Python is implemented in a hash table, it has a time complexity of O(1) for every insert attempt, making finding a union of two sets just the set() of all values in both lists.
# Thus the union of two linked lists is O(n+m) in length n and m sets. Then the union set is turned into a new linked list which takes O(n) time for n items in the union set.
# Since both linked lists are sets, we do not need to worry about duplicate values
def union(llist_1, llist_2):
    union_set = set()
    ll_node = llist_1.head
    while ll_node:
        union_set.add(ll_node.value)
        ll_node = ll_node.next
    ll_node = llist_2.head
    while ll_node:
        union_set.add(ll_node.value)
        ll_node = ll_node.next
    union_set_ll = LinkedList()
    for item in union_set:
        union_set_ll.append(item)
    return(union_set_ll)

# Initiating two sets takes O(n+m) time for length n and m of llist_1 and llist_2
# Then the built in set1.intersection(set2) function in Python operates in O(min(n, m)) time because for each value in the smaller set, it checks whether that value exist in the larger set in O(1) time.
# Creating a new linked list of the intersection takes O(n) time in n elements of the intersection set
def intersection(llist_1, llist_2):
    set1 = set()
    set2 = set()
    ll_node = llist_1.head
    while ll_node:
        set1.add(ll_node.value)
        ll_node = ll_node.next
    ll_node = llist_2.head
    while ll_node:
        set2.add(ll_node.value)
        ll_node = ll_node.next
    intersection = set1.intersection(set2)
    intersection_ll = LinkedList()
    for item in intersection:
        intersection_ll.append(item)
    return(intersection_ll)


# In the provided test cases, there contains duplicate values. However the problem also states that the goal is to find the union and intersection of two sets, which is normally defined as unique value.
# Thus in this solution, duplicate unions and intersected values are ignored
# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print ("union of ll1 and ll2 is", union(linked_list_1,linked_list_2), "with size", union(linked_list_1,linked_list_2).size(), "\n")
print ("intersection of ll1 and ll2 is", intersection(linked_list_1,linked_list_2), "with size", intersection(linked_list_1,linked_list_2).size(), "\n")

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print ("union of ll3 and ll4 is", union(linked_list_3,linked_list_4), "with size", union(linked_list_3,linked_list_4).size(), "\n")
print ("intersection of ll3 and ll4 is", intersection(linked_list_3,linked_list_4), "with size", intersection(linked_list_3,linked_list_4).size(), "\n")

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1: Finding the union and intersection of two lists consisting of [None, ""]
print("Test Case 1: ")
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()
element_1 = [None, '']
element_2 = [None, '']
for i in element_1:
    linked_list_5.append(i)
for i in element_2:
    linked_list_6.append(i)
print("union of ll5 and ll6 is", union(linked_list_5,linked_list_6), "with size", union(linked_list_5,linked_list_6).size(), "\n")
print("intersection of ll5 and ll6 is", intersection(linked_list_5,linked_list_6), "with size", intersection(linked_list_5,linked_list_6).size(), "\n")

# Test Case 2: Inputs are two lists of prime and non-prime numbers up to 100. The two lists should have no intersection and should have a union of all natural numbers up to 100.
print("Test Case 2: ")
primes = set()
def is_prime(n):
    for prime in primes:
        if prime > math.floor(math.sqrt(n)):
            primes.add(n)
            return(True)
        elif n % prime == 0 and n != prime:
            return(False)

prime_ll = LinkedList()
not_prime_ll = LinkedList()
        
for i in range(1, 101):
    if is_prime(i) == True:

        prime_ll.append(i)
    else:
        not_prime_ll.append(i)

print("union of ll7 and ll8 is", union(prime_ll, not_prime_ll), "\n")
print("intersection of ll7 and ll8 is", intersection(prime_ll, not_prime_ll), "\n")
print(f"The length of the union of prime and non-prime natural numbers up to 100 should equal 100 and equals {union(prime_ll, not_prime_ll).size()}\n")
print(f"The length of the intersection of prime and non-prime natural numbers up to 100 should equal 0 and equals {intersection(prime_ll, not_prime_ll).size()}\n")

# Test Case 3: Determining the union of the Fibonnacci Sequence and prime numbers up to ten million (10000000)
print("Test Case 3: ")
fibonacci_sequence = LinkedList()
fibo_last_2 = 0
fibo_last_1 = 1
fibonacci_sequence.append(fibo_last_2)
fibonacci_sequence.append(fibo_last_1)
fibo_next = fibo_last_2 + fibo_last_1
while fibo_next <= 10000000:
    fibo_next = fibo_last_2 + fibo_last_1
    fibo_last_2 = fibo_last_1
    fibo_last_1 = fibo_next
    fibonacci_sequence.append(fibo_next)
prime_ll = LinkedList()
for i in range(1, 10000001):
    if is_prime(i):
        prime_ll.append(i) 
print(f"The union of the Fibonnacci Sequence and prime numbers up to ten million have a length of {union(prime_ll, fibonacci_sequence).size()}!\n")
print(f"They are: {union(prime_ll, fibonacci_sequence)}\n")