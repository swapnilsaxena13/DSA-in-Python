# String Operations in Python - Part 1

# Python offers two membership operators to check if a value exists in a sequence like strings, lists, or tuples.

# 'in' operator: Returns True if the specified element exists in the sequence, otherwise False.
# 'not in' operator: Returns True if the element is NOT found in the sequence, otherwise False.

# Example:
s1 = "geeksforgeeks"
s2 = "geeks"

print(s2 in s1)  # True
print(s2 not in s1)  # False

# -------------------------------------------------------------
# String Concatenation using + Operator
# The + operator is used to join multiple strings together.
# Note: All operands must be strings.

s1 = "geeks"
s2 = "for"
s3 = s1 + s2  # Concatenates s1 and s2
s4 = "welcome to " + s1 + s2  # Concatenates multiple strings

print(s3)  # Output: geeksfor
print(s4)  # Output: welcome to geeksfor

# -------------------------------------------------------------
# Finding a Substring in a String using index() and rindex()
# index() - Returns the first occurrence index of the substring.
# rindex() - Returns the last occurrence index of the substring.
# index(start, end) - Searches within a specific range.

s1 = "geeksforgeeks"
s2 = "geeks"

print(s1.index(s2))  # Output: 0 (First occurrence of 'geeks')
print(s1.rindex(s2))  # Output: 8 (Last occurrence of 'geeks')
print(s1.index(s2, 1, 13))  # Output: 8 (Search within index range 1 to 13)

# Note:
# - If the substring is not found, index() raises a ValueError.
# - The rindex() method is useful when searching from the end.
# - Always handle exceptions when using index() in real applications to avoid crashes.
