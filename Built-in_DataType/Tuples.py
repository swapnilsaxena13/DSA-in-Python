# Python Tuples - Comprehensive Guide

"""
Tuple Basics:
- Tuples are used to store multiple items in a single variable.
- They are one of 4 built-in data types in Python for collections:
  - List: ordered, changeable, allows duplicates
  - Tuple: ordered, unchangeable, allows duplicates
  - Set: unordered, unchangeable*, unindexed, no duplicates
  - Dictionary: ordered**, changeable, no duplicates
- Tuples are written with round brackets.
"""

# ==================== CREATING TUPLES ====================

# Basic tuple creation
fruits = ("apple", "banana", "cherry")
print(fruits)  # Output: ('apple', 'banana', 'cherry')

# Tuple with duplicate values
duplicate_tuple = ("apple", "banana", "cherry", "apple", "cherry")
print(duplicate_tuple)  # Output: ('apple', 'banana', 'cherry', 'apple', 'cherry')

# Tuple length
print(len(fruits))  # Output: 3

# Single-item tuple (note the trailing comma)
single_item = ("apple",)
print(type(single_item))  # Output: <class 'tuple'>

# NOT a tuple (without comma)
not_a_tuple = ("apple")
print(type(not_a_tuple))  # Output: <class 'str'>

# Tuple with different data types
mixed_tuple = ("abc", 34, True, 40, "male")
print(mixed_tuple)  # Output: ('abc', 34, True, 40, 'male')

# Using the tuple() constructor
constructed_tuple = tuple(("apple", "banana", "cherry"))
print(constructed_tuple)  # Output: ('apple', 'banana', 'cherry')

# ==================== ACCESSING TUPLE ITEMS ====================

"""
Tuple items are:
- Ordered (maintain their order)
- Indexed (first item is index 0)
- Unchangeable (cannot modify after creation)
"""

# Access by index
print(fruits[1])  # Output: banana

# Negative indexing (starts from end)
print(fruits[-1])  # Output: cherry

# Range of indexes (returns new tuple)
numbers = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(numbers[2:5])  # Output: ('cherry', 'orange', 'kiwi') (5 not included)

# From beginning to index
print(numbers[:4])  # Output: ('apple', 'banana', 'cherry', 'orange')

# From index to end
print(numbers[2:])  # Output: ('cherry', 'orange', 'kiwi', 'melon', 'mango')

# Negative range
print(numbers[-4:-1])  # Output: ('orange', 'kiwi', 'melon') (-1 not included)

# Check if item exists
if "apple" in fruits:
    print("Yes, 'apple' is in the fruits tuple")  # Output: Yes, 'apple' is in the fruits tuple

# ==================== UPDATING TUPLES ====================

"""
Tuples are unchangeable, but we can work around this by:
1. Converting to list, modifying, then converting back
2. Adding tuples together
"""

# Changing a tuple (indirectly)
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)  # Output: ('apple', 'kiwi', 'cherry')

# Adding items (method 1: convert to list)
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)  # Output: ('apple', 'banana', 'cherry', 'orange')

# Adding items (method 2: add tuple to tuple)
thistuple = ("apple", "banana", "cherry")
y = ("orange",)  # Note the comma for single-item tuple
thistuple += y
print(thistuple)  # Output: ('apple', 'banana', 'cherry', 'orange')

# ==================== REMOVING ITEMS ====================

"""
Note: You cannot directly remove items from tuples, but you can:
1. Convert to list, remove items, convert back
2. Delete the tuple completely
"""

# Removing items (indirectly)
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)  # Output: ('banana', 'cherry')

# Deleting a tuple completely
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple)  # This would raise an error as tuple no longer exists

# ==================== UNPACKING TUPLES ====================

"""
Packing a tuple: assigning values to a tuple
Unpacking a tuple: extracting values back into variables
"""

# Packing a tuple
fruits = ("apple", "banana", "cherry")

# Unpacking a tuple
(green, yellow, red) = fruits
print(green)   # Output: apple
print(yellow)  # Output: banana
print(red)     # Output: cherry

"""
Note: Number of variables must match number of values.
If not, use * to collect remaining values as list.
"""

# Using asterisk (*) to collect remaining values
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)  # Output: apple
print(yellow) # Output: banana
print(red)    # Output: ['cherry', 'strawberry', 'raspberry']

# Asterisk with middle variable
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)  # Output: apple
print(tropic) # Output: ['mango', 'papaya', 'pineapple']
print(red)    # Output: cherry

# ==================== LOOPING THROUGH TUPLES ====================

# Using for loop
thistuple = ("apple", "banana", "cherry")
print("For loop:")
for x in thistuple:
    print(x)
# Output:
# apple
# banana
# cherry

# Using for loop with index
print("\nFor loop with index:")
for i in range(len(thistuple)):
    print(thistuple[i])
# Output:
# apple
# banana
# cherry

# Using while loop
print("\nWhile loop:")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1
# Output:
# apple
# banana
# cherry

# ==================== JOINING TUPLES ====================

# Joining with + operator
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)  # Output: ('a', 'b', 'c', 1, 2, 3)

# Multiplying tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)  # Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

# ==================== TUPLE METHODS ====================

"""
Python has two built-in tuple methods:
1. count() - returns number of times a value occurs
2. index() - searches for value and returns first position found
"""

# count() method
numbers = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5, 7)
count_of_7 = numbers.count(7)
print(count_of_7)  # Output: 3

# index() method
first_occurrence_of_7 = numbers.index(7)
print(first_occurrence_of_7)  # Output: 2

# Note: index() can take start and end parameters
second_occurrence_of_7 = numbers.index(7, 3)  # Start searching from index 3
print(second_occurrence_of_7)  # Output: 4