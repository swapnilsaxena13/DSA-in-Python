"""
Strings in Python
-----------------

In Python, strings are sequences of characters represented using Unicode.
Python does not have a dedicated character data type; a single character is simply a string of length 1.
Strings are immutable, meaning their elements cannot be changed once assigned.
"""

# Example of defining a string
a = "Geeksforgeeks"  # Using double quotes
b = 'Geeksforgeeks'  # Using single quotes
print(a)
print(b)

"""
Order and Character Representation
----------------------------------
Python provides functions to convert characters to their corresponding ASCII/Unicode values and vice versa:
  - `ord(char)`: Returns the Unicode code of a character.
  - `chr(int)`: Converts an integer (ASCII/Unicode) back to a character.
"""

# Example
print(ord("A"))  # Character 'A' to ASCII (65)
print(ord("Z"))  # Character 'Z' to ASCII (90)

print(ord("a"))  # Character 'a' to ASCII (97)
print(ord("z"))  # Character 'z' to ASCII (122)

print(chr(97))   # ASCII 97 to character ('a')
print(chr(65))   # ASCII 65 to character ('A')

"""
Indexing in Strings
--------------------
Strings support indexing, allowing access to specific characters.
  - Positive indexing starts from 0.
  - Negative indexing starts from -1 (last character).
"""

s = "geek"
print(s)       # Prints entire string
print(s[0])    # First character ('g')
print(s[-1])   # Last character ('k')
print(s[1])    # Second character ('e')
print(s[-2])   # Second last character ('e')

"""
Strings are Immutable
----------------------
Once a string is created, its contents cannot be modified directly.
Attempting to change a character will result in an error.
"""

s = "geek"
# s[0] = "e"  # Uncommenting this will cause an error: TypeError: 'str' object does not support item assignment
print(s)  # Strings remain unchanged

"""
Multiline Strings
-----------------
Multiline strings can be created using triple quotes ('''  ''' or """  """).
They are often used for multi-line text or documentation strings (docstrings).
"""

s = """Hi,
This is a Python course.
Hope you are enjoying it."""
print(s)