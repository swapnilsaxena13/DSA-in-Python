# TUPLES IN PYTHON 🍇🍉🍒
# ----------------------
# Tuples are used to store multiple items in a single variable.
# Tuples are ordered, unchangeable (immutable), and allow duplicates.
# They are written with round brackets.

# Creating a tuple
mytuple = ("apple", "banana", "cherry")
print(mytuple)

# Tuple items are ordered, unchangeable, and allow duplicate values
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Length of a tuple
print(len(thistuple))

# Tuple with one item: must include a comma!
thistuple = ("apple",)
print(type(thistuple))  # Output: <class 'tuple'>

# Not a tuple: no comma
thistuple = ("apple")
print(type(thistuple))  # Output: <class 'str'>

# Tuples can contain any data type
tuple1 = ("apple", "banana", "cherry")  # str
tuple2 = (1, 5, 7, 9, 3)               # int
tuple3 = (True, False, False)         # bool

# Tuple with mixed data types
tuple4 = ("abc", 34, True, 40, "male")
print(type(tuple4))

# Creating a tuple using the tuple() constructor
thistuple = tuple(("apple", "banana", "cherry"))  # double round-brackets
print(thistuple)

# ---------------------
# ACCESSING TUPLE ITEMS
# ---------------------
print(thistuple[1])   # Access using index
print(thistuple[-1])  # Negative indexing (last item)
print(thistuple[2:5]) # Range of indexes
print(thistuple[:4])  # Items from start to index 3
print(thistuple[2:])  # Items from index 2 to end

# Negative range
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])  # Outputs: ('orange', 'kiwi', 'melon')

# ---------------------
# CHECK IF ITEM EXISTS
# ---------------------
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

# ---------------------
# CHANGE TUPLE VALUES
# ---------------------
# Tuples are immutable, but we can convert them to a list to modify

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# ---------------------
# ADD ITEMS TO A TUPLE
# ---------------------
# Method 1: Convert to list and use append()
y = list(x)
y.append("orange")
x = tuple(y)
print(x)

# Method 2: Concatenate tuples
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

# ---------------------
# REMOVE ITEMS FROM TUPLE
# ---------------------
# Convert to list and remove
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# ---------------------
# UNPACKING TUPLES
# ---------------------
# You can extract tuple values into variables
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Unpacking with *
# The asterisk (*) can collect the remaining values
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)  # Output: ['cherry', 'strawberry', 'raspberry']

# Asterisk in the middle
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

# ---------------------
# LOOP THROUGH A TUPLE
# ---------------------
# Using a for loop
for x in fruits:
    print(x)

# Loop through the index numbers
for i in range(len(fruits)):
    print(fruits[i])

# Using while loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# ---------------------
# JOINING TUPLES
# ---------------------
# Using + operator
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

# ---------------------
# TUPLE METHODS
# ---------------------
# Tuples have only two built-in methods:
# 1. count() – Returns the number of times a value appears
# 2. index() – Searches the tuple for a specified value and returns the position

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple.count("apple"))  # Output: 2
print(thistuple.index("cherry"))  # Output: 2
