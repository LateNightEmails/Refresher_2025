from collections import Counter
from collections import defaultdict
from collections import deque

# Practice Collections in Python

# List
print("List Example:")
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)
my_list.append(6)
print("After Append:", my_list)
my_list.remove(3)
print("After Remove:", my_list)
print()

# Tuple
print("Tuple Example:")
my_tuple = (1, 2, 3, 4, 5)
print("Original Tuple:", my_tuple)
# Tuples are immutable, so we cannot append or remove elements
# my_tuple.append(6)  # This will raise an AttributeError
# my_tuple.remove(3)  # This will raise an AttributeError
print()

# Set
print("Set Example:")
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)
my_set.add(6)
print("After Add:", my_set)
my_set.remove(3)
print("After Remove:", my_set)
print()

# Dictionary
print("Dictionary Example:")
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original Dictionary:", my_dict)
my_dict['d'] = 4
print("After Adding Key-Value Pair:", my_dict)
del my_dict['b']
print("After Deleting Key-Value Pair:", my_dict)
print()

# Counter from collections module
print("Counter Example:")
my_counter = Counter([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
print("Original Counter:", my_counter)
my_counter.update([1, 2, 2, 5])
print("After Update:", my_counter)
print()

# defaultdict from collections module
print("defaultdict Example:")
my_defaultdict = defaultdict(int)
my_defaultdict['a'] += 1
my_defaultdict['b'] += 2
print("defaultdict with default int:", my_defaultdict)
print()

# deque from collections module
print("deque Example:")
my_deque = deque([1, 2, 3, 4, 5])
print("Original deque:", my_deque)
my_deque.append(6)
print("After Append:", my_deque)
my_deque.appendleft(0)
print("After Appendleft:", my_deque)
my_deque.pop()
print("After Pop:", my_deque)
my_deque.popleft()
print("After Popleft:", my_deque)
print()