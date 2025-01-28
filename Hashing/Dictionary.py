# Creating a Dictionary
# Keys must be unique and immutable; values can be of any data type
d = {110: 'abc', 101: 'xyz', 105: 'pqr'}
print(d)  # Output: {110: 'abc', 101: 'xyz', 105: 'pqr'}

# Adding elements to an empty dictionary
d = {}
d['laptop'] = 40000
d['mobile'] = 15000
d['earphone'] = 1000
print(d)  # Output: {'laptop': 40000, 'mobile': 15000, 'earphone': 1000}

# Accessing a value using a key
print(d['mobile'])  # Output: 15000

# Using .get() to safely access values
d = {110: 'abc', 101: 'xyz', 105: 'pqr'}
print(d.get(101))  # Output: xyz
print(d.get(125))  # Output: None
print(d.get(125, "NA"))  # Output: NA

# Checking for the existence of a key before accessing
if 125 in d:
    print(d[125])
else:
    print("NA")  # Output: NA

# Modifying and removing elements in a dictionary
d = {110: 'abc', 101: 'xyz', 105: 'pqr', 106: 'bcd'}
d[101] = 'wxy'  # Modify value for key 101
print(len(d))  # Output: 4
print(d)  # Output: {110: 'abc', 101: 'wxy', 105: 'pqr', 106: 'bcd'}

# Removing an element using pop()
print('Returning and removing 105:', d.pop(105))  # Output: Returning and removing 105: pqr
print('After removing 105:', d)  # Output: {110: 'abc', 101: 'wxy', 106: 'bcd'}

# Removing an element using del
del d[106]
print(d)  # Output: {110: 'abc', 101: 'wxy'}

# Adding and removing the last inserted element using popitem()
d[108] = 'cde'
print('Returning and removing last inserted:', d.popitem())  # Output: Returning and removing last inserted: (108, 'cde')

# Final state of dictionary
print(d)  # Output: {110: 'abc', 101: 'wxy'}

# Important Notes:
# 1. Dictionary keys must be unique and immutable (e.g., numbers, strings, tuples).
# 2. Values in dictionaries can be duplicated and of any data type.
# 3. Keys are case-sensitive (e.g., 'Key' and 'key' are different).
# 4. Use .get() to avoid KeyError when accessing non-existent keys.
# 5. Average time complexity for insert, search, and delete: O(1).
# 6. Worst-case time complexity: O(n) due to hash collisions.
