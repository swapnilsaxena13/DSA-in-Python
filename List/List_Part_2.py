"""
### Python Concepts Demonstrated in This File ###
1. Looping Through a List
2. Using the range() Function
3. Creating a List of Numbers with range()
4. Simple Statistics with a List of Numbers
5. List Comprehensions
6. Slicing a List
7. Looping Through a Slice
8. Copying a List
9. Tuples - Immutable Data Structures
"""

# Looping Through an Entire List
magicians = ['alice', 'david', 'carolina']
print("Looping through a list of magicians:")
for magician in magicians:
    print(magician)  # Loop through each item in the list

# Using the range() Function
print("\nUsing the range() function to generate numbers from 1 to 4:")
for value in range(1, 5):  # range() generates numbers starting from 1 up to (but not including) 5
    print(value)

# Using range() to Make a List of Numbers
numbers = list(range(1, 6))  # Converts range object to a list
print("\nCreating a list of numbers using range():", numbers)

# Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("\nSimple statistics with a list of digits:")
print(f"Minimum value: {min(digits)}")  # Minimum value in the list
print(f"Maximum value: {max(digits)}")  # Maximum value in the list
print(f"Sum of all digits: {sum(digits)}")  # Sum of all numbers in the list

# List Comprehensions
print("\nUsing list comprehensions to create a list of squares:")
squares = [value**2 for value in range(1, 11)]  # List comprehension to generate squares of 1-10
print(squares)

# Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("\nSlicing a list to get the first three players:")
print(players[0:3])  # Slicing from index 0 to 2 (3 is excluded)

# Looping Through a Slice
print("\nLooping through the first three players in the list:")
for player in players[:3]:  # Slicing and looping through the first 3 players
    print(player.title())  # .title() capitalizes the first letter of the string

# Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # Copying the list using slicing
print("\nCopying a list:")
print("My favorite foods are:", my_foods)
print("My friend's favorite foods are:", friend_foods)

# Tuples - Immutable Data Structures
dimensions = (200, 50)  # Tuple: immutable list
print("\nTuples - Immutable data structures:")
print("Original dimensions:")
for dimension in dimensions:  # Loop through tuple items
    print(dimension)

# Modifying a Tuple by Redefining It
dimensions = (400, 100)  # Re-assigning a new tuple
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
