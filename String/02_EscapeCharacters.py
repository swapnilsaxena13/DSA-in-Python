"""
Escape Sequences and Raw Strings in Python
------------------------------------------

Escape sequences allow the inclusion of special characters in strings using a backslash (\).
Common escape sequences include:
  - `\n` : Newline
  - `\t` : Tab
  - `\'` : Single quote
  - `\"` : Double quote
  - `\\` : Backslash

Raw strings (`r"string"`) treat backslashes as literal characters, useful for file paths.
"""

# Example of escape sequences
s1 = 'Welcome to Geek\'s course'  # Using backslash to escape single quote
print(s1)

s2 = "Hi \nwelcome to the course"  # Newline escape sequence
print(s2)

# More examples of escape sequences
s3 = "A simple \\ example"  # Double backslash to include a backslash
print(s3)
s4 = "Backslash at the end\\"
print(s4)
s5 = "\\n"  # Prints "\n" instead of interpreting as newline
print(s5)
s6 = "\\t"  # Prints "\t" instead of interpreting as tab
print(s6)

"""
Raw Strings
-----------

Raw strings treat backslashes as normal characters, useful for Windows file paths.
"""

s7 = "c:\\project\\name.py"  # Regular string, `\n` is treated as newline
print(s7)

s8 = r"c:\\project\\name.py"  # Raw string, treats `\n` as normal characters
print(s8)
