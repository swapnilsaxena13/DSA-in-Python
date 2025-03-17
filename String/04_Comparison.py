# String Comparison in Python

# Method 1: Using Relational Operators
# The relational operators compare the Unicode values of characters in strings
# from the first character to the last.
# If a difference is found, the comparison is determined based on Unicode values.

s1 = "geeksforgeeks"
s2 = "ide"

# Comparing two strings using relational operators
print(s1 < s2)   # True  (Unicode comparison)
print(s1 <= s2)  # True  (Unicode comparison)
print(s1 > s2)   # False (Unicode comparison)
print(s1 >= s2)  # False (Unicode comparison)
print(s1 == s2)  # False (Strings are different)
print(s1 != s2)  # True  (Strings are different)

print("#############")

# Additional comparisons
print("abcd > abc ", "abcd" > "abc")  # True ("abcd" has an extra character)
print("ZAB > ABC", "ZAB" > "ABC")      # True (Unicode of 'Z' > 'A')
print("abc > ABC ", "abc" > "ABC")      # True (Unicode of 'a' > 'A')
print("x > abcd", "x" > "abcd")        # True (Unicode of 'x' > 'a')

# Notes:
# - String comparisons in Python are case-sensitive.
# - Uppercase letters have lower Unicode values than lowercase letters.
# - The comparison stops as soon as a mismatch is found.
# - If one string is a prefix of another, the longer string is considered greater.
# - Use str.lower() or str.upper() for case-insensitive comparisons.
