'''
A string is a series of characters. Anything inside quotes is considered 
a string in Python, and you can use single or double quotes around your 
strings like this: 
'''

"This is a string."
'This is also a string.'


# Changing Case in a String with Methods
name="ada lovelace"
print(name.title())

name="Ada Lovelace"
print(name.upper())
print(name.lower())

# Original string
s = "abc"

# Convert string into a list where each character becomes an element
s_list = list(s)

# Print the lista
print(s_list)  # Output: ['a', 'b', 'c']

# Accessing individual characters from the list
print(s_list[0])  # Output: 'a'
print(s_list[1])  # Output: 'b'
print(s_list[2])  # Output: 'c'


# Using Variables in Strings

first_name="ada"
last_name="lovelace"
full_name=f"{first_name.title()} {last_name.title()}"
print(full_name)

#Adding Whitespace to Strings with Tabs or Newlines
"""To add a tab to your text, use the character combination \t as shown :"""
print("Python") 

print("\tPython") 

"""To add a newline in a string, use the character combination \n:"""
print("Languages:\nPython\nC\nJavaScript") 

# Stripping Whitespace
"""You can also strip whitespace from the left side and right side of a string using the 
lstrip() method and rstrip() method, or from both sides at once using strip():"""
favorite_language = '  python  ' 

print(favorite_language.rstrip()+"abc")

print(favorite_language.lstrip()+"abc")

print(favorite_language.strip()+"abc")

# Avoiding Syntax Errors with Strings

"""Here’s how to use single and double quotes correctly. Save this program 
as apostrophe.py and then run it:"""
message = "One of Python's strengths is its diverse community." 
print(message)