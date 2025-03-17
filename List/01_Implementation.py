# Python Lists: Introduction and Operations

# A list in Python is a collection of items that are ordered and mutable (can be changed).
# Lists are one of the most versatile data structures in Python and can hold elements of different data types.
# Lists are created using square brackets [], and elements are separated by commas.

# Example of a List
my_list = ["Geeks", "for", "Geeks"]
print(my_list)  # Output: ["Geeks", "for", "Geeks"]

# Key Characteristics of Lists:
# 1. Ordered: Elements maintain their order.
# 2. Mutable: Elements can be added, removed, or modified.
# 3. Heterogeneous: Can contain elements of different data types (e.g., integers, strings, objects).
# 4. Dynamic: Size can grow or shrink as needed.

# ------------------------------------------
# Creating a List
# ------------------------------------------

# 1. Empty List
empty_list = []
print("Blank List:", empty_list)  # Output: []

# 2. List with Numbers
num_list = [10, 20, 14]
print("List of Numbers:", num_list)  # Output: [10, 20, 14]

# 3. List with Strings
str_list = ["Geeks", "For", "Geeks"]
print("List of Strings:", str_list)  # Output: ["Geeks", "For", "Geeks"]

# 4. List with Mixed Data Types
mixed_list = [1, 2, "Geeks", 4, "For", 6, "Geeks"]
print("Mixed List:", mixed_list)  # Output: [1, 2, "Geeks", 4, "For", 6, "Geeks"]

# 5. List with Duplicate Elements
duplicate_list = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("List with Duplicates:", duplicate_list)  # Output: [1, 2, 4, 4, 3, 3, 3, 6, 5]

# ------------------------------------------
# Accessing Elements from a List
# ------------------------------------------

# Elements in a list can be accessed using their index.
# Python uses 0-based indexing, meaning the first element is at index 0.

# Example 1: Accessing Elements
l = [10, 20, 30, 40, 50]
print("Element at index 3:", l[3])  # Output: 40
print("Element at index 1:", l[1])  # Output: 20

# Negative Indexing: Access elements from the end of the list.
print("Last element:", l[-1])  # Output: 50
print("Second last element:", l[-2])  # Output: 40

# Example 2: Accessing Elements in a Multi-Dimensional List
multi_dim_list = [['Geeks', 'For'], ['Geeks']]
print("Element at [0][1]:", multi_dim_list[0][1])  # Output: For
print("Element at [1][0]:", multi_dim_list[1][0])  # Output: Geeks

# ------------------------------------------
# Getting the Size of a List
# ------------------------------------------

# The len() function is used to get the number of elements in a list.
print("Length of num_list:", len(num_list))  # Output: 3
print("Length of empty_list:", len(empty_list))  # Output: 0

# ------------------------------------------
# Adding Elements to a List
# ------------------------------------------

# Method 1: Using append()
# Adds an element to the end of the list.
num_list.append(30)
print("After append:", num_list)  # Output: [10, 20, 14, 30]

# Method 2: Using insert()
# Inserts an element at a specific index.
num_list.insert(1, 15)
print("After insert:", num_list)  # Output: [10, 15, 20, 14, 30]

# Method 3: Using extend()
# Adds multiple elements to the end of the list.
num_list.extend([40, 50])
print("After extend:", num_list)  # Output: [10, 15, 20, 14, 30, 40, 50]

# ------------------------------------------
# Removing Elements from a List
# ------------------------------------------

# Method 1: Using remove()
# Removes the first occurrence of a specific value.
num_list.remove(15)
print("After remove:", num_list)  # Output: [10, 20, 14, 30, 40, 50]

# Method 2: Using pop()
# Removes and returns the element at a specific index (default is the last element).
popped_element = num_list.pop()
print("Popped element:", popped_element)  # Output: 50
print("After pop:", num_list)  # Output: [10, 20, 14, 30, 40]

# Method 3: Using del
# Deletes an element at a specific index or a slice of elements.
del num_list[2]
print("After del:", num_list)  # Output: [10, 20, 30, 40]

# ------------------------------------------
# Reversing a List
# ------------------------------------------

# Using reverse()
num_list.reverse()
print("Reversed List:", num_list)  # Output: [40, 30, 20, 10]

# ------------------------------------------
# Sorting a List
# ------------------------------------------

# Using sort()
num_list.sort()
print("Sorted List:", num_list)  # Output: [10, 20, 30, 40]

# ------------------------------------------
# List Methods Summary
# ------------------------------------------

# append(): Adds an element to the end of the list.
# extend(): Adds multiple elements to the end of the list.
# insert(): Inserts an element at a specific index.
# remove(): Removes the first occurrence of a specific value.
# pop(): Removes and returns an element at a specific index.
# clear(): Removes all elements from the list.
# index(): Returns the index of the first occurrence of a value.
# count(): Returns the number of occurrences of a value.
# sort(): Sorts the list in ascending order.
# reverse(): Reverses the order of elements in the list.
# copy(): Returns a shallow copy of the list.

# ------------------------------------------
# Built-in Functions with Lists
# ------------------------------------------

# sum(): Returns the sum of all elements in the list.
print("Sum of num_list:", sum(num_list))  # Output: 100

# max(): Returns the maximum element in the list.
print("Max of num_list:", max(num_list))  # Output: 40

# min(): Returns the minimum element in the list.
print("Min of num_list:", min(num_list))  # Output: 10

# len(): Returns the number of elements in the list.
print("Length of num_list:", len(num_list))  # Output: 4

# ------------------------------------------
# Taking Input for a List
# ------------------------------------------

# Example 1: Taking space-separated input as a string and converting it to a list.
input_string = input("Enter elements (Space-Separated): ")
input_list = input_string.split()
print("Input List:", input_list)

# Example 2: Taking integer input for a list.
n = int(input("Enter the size of the list: "))
int_list = list(map(int, input("Enter integer elements: ").strip().split()))[:n]
print("Integer List:", int_list)

# ------------------------------------------
# Time and Space Complexity
# ------------------------------------------

# Creating a List: O(1) time, O(n) space
# Accessing Elements: O(1) time, O(1) space
# Adding Elements:
#   - append(): O(1) time, O(1) space
#   - insert(): O(n) time, O(1) space
#   - extend(): O(n) time, O(1) space
# Removing Elements:
#   - remove(): O(n) time, O(1) space
#   - pop(): O(1) time (for last element), O(n) time (for first/middle elements), O(1) space
# Sorting: O(n log n) time, O(n) space
# Reversing: O(n) time, O(1) space