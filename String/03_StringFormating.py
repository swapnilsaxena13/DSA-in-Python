"""
String Formatting in Python
---------------------------
String formatting allows dynamic insertion of values into strings in a structured manner.
There are four primary ways to format strings in Python:

1. Formatting with % Operator
2. Formatting with format() method
3. Formatting with f-strings (formatted string literals)
4. Formatting with String Template Class (not covered in this example)
"""

# 1. Using % Operator (Old-style formatting)
name = "ABC"
course = "Python Course"
s = "Welcome %s to the %s" % (name, course)
print(s)
print()

# 2. Using format() method
s = "Welcome {0} to the {1}".format(name, course)
print(s)
print()

# 3. Using f-strings (Recommended for Python 3.6+)
s = f"Welcome {name} to the {course}"
print(s)
print()

"""
All three methods produce the same output:
Welcome ABC to the Python Course
"""

# Mathematical operations using f-strings
a = 10
b = 20
print(f"Sum of {a} and {b} is {a + b}")
print(f"Product of {a} and {b} is {a * b}")

"""
Output:
Sum of 10 and 20 is 30
Product of 10 and 20 is 200
"""

# String case conversion using f-strings
s1 = "ABC"
s2 = "abc"
print(f"Lower case of {s1} is {s1.lower()}")
print(f"Upper case of {s2} is {s2.upper()}")

"""
Output:
Lower case of ABC is abc
Upper case of abc is ABC

Note:
- f-strings are the most recommended method due to their readability and efficiency.
- The % operator is considered outdated and is generally avoided.
- The format() method is flexible but less concise than f-strings.
"""
