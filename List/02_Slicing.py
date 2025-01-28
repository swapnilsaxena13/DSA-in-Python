# Slicing in Python

# Slicing Syntax: sequence[start:stop:step]
# start - The index where the slice starts (inclusive)
# stop - The index where the slice ends (exclusive)
# step - The difference between each index in the slice (optional)

# Indexing in Sequences:
# Sequences in Python are indexed starting from 0 for the first element.
# Negative indexing starts from -1 for the last element, -2 for the second last, and so on.

# Initialize list
my_list = [10, 20, 30, 40, 50, 60, 70]

# 1. Slicing without start, stop, and step (returns the entire list)
print(my_list[:])

# 2. Slicing with start (from index 2 to the end)
print(my_list[2:])

# 3. Slicing with stop (from beginning to index 4)
print(my_list[:4])

# 4. Slicing with step (every second element)
print(my_list[0:7:2])

# 5. Slicing with negative step (reversing the list)
print(my_list[-3:-8:-1])

# 6. Slicing with start and step (from index 1 to end, every third element)
print(my_list[1::3])

# 7. Slicing with stop and step (from beginning to index 6, every two elements)
print(my_list[:6:2])

# 8. Slicing with negative indices (from index -5 to -2)
print(my_list[-5:-2])

# 9. Slicing to reverse a string using shortcut
my_string = "Python"
print(my_string[::-1])

# 10. Slicing a tuple with start, stop, and step
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(my_tuple[::3])

# Slicing in List
# List slicing creates a new list and does not modify the original list.
Lst = [50, 70, 30, 20, 90, 10, 50]
print(Lst[1:5])

# Slicing in Tuple
# Tuple slicing works the same way, but tuples are immutable.
tup = (22, 3, 45, 4, 2.4, 2, 56, 890, 1)
print(tup[1:4])

# Slicing Differences Between List, Tuple, and String
# When slicing a list, a new list is created (different object).
# When slicing a tuple or string, the same object is returned due to immutability.
l1 = [10, 20, 30]
l2 = l1[:]
t1 = (10, 20, 30)
t2 = t1[:]
s1 = "geeks"
s2 = s1[:]
print(l1 is l2)  # False (different objects)
print(t1 is t2)  # True (same object)
print(s1 is s2)  # True (same object)
