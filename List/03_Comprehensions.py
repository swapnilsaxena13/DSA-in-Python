# Python Comprehensions
# Comprehensions provide a concise way to create sequences (lists, sets, dictionaries, generators) from existing sequences.

# 1. List Comprehensions
# Provides an elegant way to create new lists.
# Basic Structure: output_list = [output_exp for var in input_list if (var satisfies this condition)]
# Note that list comprehension may or may not contain an if condition.
# List comprehensions can contain multiple for loops (nested list comprehensions).

# Example 1: Creating a list of even numbers from an input list
l = [1, 2, 3, 4, 5]
l1 = [x for x in l if x % 2 == 0]
print(l1)  # Output: [2, 4]

# Creating a list of odd numbers from an input list
l2 = [x for x in l if x % 2 != 0]
print(l2)  # Output: [1, 3, 5]

# Another example
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
list_using_comp = [var for var in input_list if var % 2 == 0]
print("Output List using list comprehensions:", list_using_comp)
# Output: [2, 4, 4, 6]


# 2. Dictionary Comprehensions
# Dictionary comprehensions allow us to create dictionaries in a concise way.
# Basic Structure: output_dict = {key:value for (key, value) in iterable if (key, value satisfy this condition)}

# Example 1: Creating a dictionary with numbers and their cubes
d1 = {x: x**3 for x in [1, 3, 4, 2, 5]}
print(d1)

# Creating a dictionary using range
d2 = {x: f"ID{x}" for x in range(5)}
print(d2)  # Output: {0: 'ID0', 1: 'ID1', 2: 'ID2', 3: 'ID3', 4: 'ID4'}

# Creating a dictionary by zipping two lists
l2 = [101, 103, 102]
l3 = ['gfg', 'ide', 'corse']
d3 = {l2[i]: l3[i] for i in range(len(l2))}
print(d3)

# Using dict and zip function
d4 = dict(zip(l2, l3))
print(d4)

# Another example
input_list = [1, 2, 3, 4, 5, 6, 7]
dict_using_comp = {var: var ** 3 for var in input_list if var % 2 != 0}
print("Output Dictionary using dictionary comprehensions:", dict_using_comp)
# Output: {1: 1, 3: 27, 5: 125, 7: 343}


# 3. Set Comprehensions
# Similar to list comprehensions but use curly brackets {}
# Note that set comprehensions discard duplicate values.

# Example 1: Creating a set of even numbers
l = {10, 20, 3, 4, 10, 20, 7, 3}
s1 = {x for x in l if x % 2 == 0}
print(s1)  # Output: {10, 4, 20}

# Creating a set of odd numbers
s2 = {x for x in l if x % 2 != 0}
print(s2)  # Output: {3, 7}

# Another example
input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
set_using_comp = {var for var in input_list if var % 2 == 0}
print("Output Set using set comprehensions:", set_using_comp)
# Output: {2, 4, 6}


# 4. Inverting Dictionary
# Key becomes value and value becomes key

d1 = {101: 'gfg', 103: 'practice', 102: 'ide'}
d2 = {v: k for (k, v) in d1.items()}
print(d2)
# Output: {'gfg': 101, 'practice': 103, 'ide': 102}


# 5. Generator Comprehensions
# Generator comprehensions are similar to list comprehensions but use round brackets ()
# Generators don’t allocate memory for the whole list, instead they generate values one by one.
# They are memory efficient.

input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
output_gen = (var for var in input_list if var % 2 == 0)

print("Output values using generator comprehensions:", end=' ')
for var in output_gen:
    print(var, end=' ')
# Output: 2 4 4 6
