"""
ENUMERATE() IN PYTHON — SHORT GUIDE

enumerate() is a built-in Python function used when you want
both the index and the value while looping through an iterable.

Normally a loop gives only values, but enumerate() gives:
    (index, value)

Syntax:
    enumerate(iterable, start=0)
"""

# -------------------------------------------------
# 1. Basic Example
# -------------------------------------------------

fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# Output:
# 0 apple
# 1 banana
# 2 mango


# -------------------------------------------------
# 2. Starting index from a different number
# -------------------------------------------------

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# Output:
# 1 apple
# 2 banana
# 3 mango


# -------------------------------------------------
# 3. What enumerate() actually returns
# -------------------------------------------------

pairs = list(enumerate(fruits))
print(pairs)

# Output:
# [(0, 'apple'), (1, 'banana'), (2, 'mango')]


# -------------------------------------------------
# 4. Without enumerate (older way)
# -------------------------------------------------

for i in range(len(fruits)):
    print(i, fruits[i])

# enumerate() is preferred because it is cleaner.


# -------------------------------------------------
# 5. Common Use Case (DSA)
# -------------------------------------------------

nums = [4, 7, 1, 9]

for i, num in enumerate(nums):
    if num == 1:
        print("Found at index:", i)


# -------------------------------------------------
# KEY IDEA
# -------------------------------------------------

"""
enumerate(list)

converts this:

["a", "b", "c"]

into:

(0, "a")
(1, "b")
(2, "c")

So you always get both:
    index and element
"""