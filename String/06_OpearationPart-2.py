
# -------------------------------------------------------------
# String Methods: isupper(), islower(), startswith(), endswith()
#
# isupper(): Returns True if all characters are uppercase, otherwise False.
# islower(): Returns True if all characters are lowercase, otherwise False.
# startswith(): Checks if a string starts with a specific substring.
# endswith(): Checks if a string ends with a specific substring.

s1 = "geeks"
print(len(s1))  # Output: 5

s2 = s1.upper()
print(s2)  # Output: GEEKS

s3 = s2.lower()
print(s3)  # Output: geeks

print(s1.islower())  # Output: True
print(s2.isupper())  # Output: True

# The isdigit() method checks if a string contains only digits (0-9).
# It returns True if all characters are numeric; otherwise, False.

print("123".isdigit())    # True (only digits)
print("abc123".isdigit()) # False (contains letters)
print("12.3".isdigit())   # False (contains a decimal point)
print("123 456".isdigit()) # False (contains a space)


s = "GeeksforGeeks Python Course"
print(s.startswith("Geeks"))  # Output: True
print(s.endswith("Course"))  # Output: True
print(s.startswith("Geeks", 1))  # Output: False
print(s.startswith("Geeks", 8, len(s)))  # Output: True

# -------------------------------------------------------------
# Splitting and Joining Strings
#
# split(): Splits a string into a list based on a delimiter.
# join(): Joins elements of a list into a string using a specified separator.
s1 = "geeks for geeks"
print(s1.split())  # Output: ['geeks', 'for', 'geeks']

s2 = "geeks, for, geeks"
print(s2.split(','))  # Output: ['geeks', ' for', ' geeks']

# join(): Joins elements of a list into a string using a specified separator.
l = ["geeksforgeeks", "python", "course"]
print(" ".join(l))  # Output: geeksforgeeks python course
print(", ".join(l))  # Output: geeksforgeeks, python, course

# -------------------------------------------------------------
# Stripping Characters from Strings
#
# strip(): Removes specified characters from both ends of a string.
# lstrip(): Removes specified characters from the left side.
# rstrip(): Removes specified characters from the right side.

s1 = "__geeksforgeeks__"
print(s1.strip("_"))  # Output: geeksforgeeks
print(s1.lstrip("_"))  # Output: geeksforgeeks__
print(s1.rstrip("_"))  # Output: __geeksforgeeks

# -------------------------------------------------------------
# Finding a Substring using find()
#
# find(): Returns the index of the first occurrence of a substring.
# Returns -1 if the substring is not found.

s1 = "geeks for geeks"
s2 = "geeks"

print(s1.find(s2))  # Output: 0
print(s1.find("gfg"))  # Output: -1
print(s1.find(s2, 1, len(s1)))  # Output: 10
