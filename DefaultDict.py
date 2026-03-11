"""
defaultdict Summary (Python)

defaultdict is a special type of dictionary from the collections module.
It behaves like a normal dictionary but automatically assigns a default
value to a key if the key does not exist.

Normal dictionary:
------------------
If you access a key that is not present, Python raises a KeyError.

Example:
    d = {}
    print(d["a"])   # KeyError

To avoid this, you normally write extra code:
    if "a" not in d:
        d["a"] = 0

defaultdict solves this problem by automatically creating the key with
a default value.
"""

from collections import defaultdict


# ---------------------------------------------------------
# 1. Basic Syntax
# ---------------------------------------------------------

"""
Syntax:

defaultdict(default_factory)

default_factory = a function that returns the default value
Examples:
    int()  -> 0
    list() -> []
    set()  -> set()
"""

d = defaultdict(int)  # default value will be 0


# ---------------------------------------------------------
# 2. Example: Counting elements (most common use)
# ---------------------------------------------------------

"""
Here defaultdict(int) automatically creates a key with value 0
if the key does not exist.
"""

arr = ["a", "b", "a", "c", "b", "a"]

count = defaultdict(int)

for ch in arr:
    count[ch] += 1  # if key doesn't exist → value starts at 0

print("Frequency count:", count)


# ---------------------------------------------------------
# 3. Example: defaultdict with list
# ---------------------------------------------------------

"""
defaultdict(list) automatically creates an empty list
when a key is accessed for the first time.
"""

d = defaultdict(list)

d["a"].append(1)
d["a"].append(2)
d["b"].append(3)

print("List defaultdict:", d)


# ---------------------------------------------------------
# 4. Example: defaultdict with set
# ---------------------------------------------------------

"""
defaultdict(set) automatically creates an empty set
when a key is accessed.
"""

d = defaultdict(set)

d["a"].add(1)
d["a"].add(2)
d["a"].add(2)  # duplicate ignored in set

print("Set defaultdict:", d)


# ---------------------------------------------------------
# 5. Example: Graph representation (very common in DSA)
# ---------------------------------------------------------

"""
defaultdict(list) is commonly used to build graph adjacency lists.
Each node automatically gets an empty list when first accessed.
"""

graph = defaultdict(list)

edges = [(1, 2), (1, 3), (2, 4)]

for u, v in edges:
    graph[u].append(v)

print("Graph:", graph)


# ---------------------------------------------------------
# 6. How defaultdict works internally
# ---------------------------------------------------------

"""
When a missing key is accessed:

defaultdict calls:
    default_factory()

Example:
    defaultdict(int)

Missing key → int() → 0

So:
    d["x"] += 1

Internally becomes:
    d["x"] = 0
    d["x"] = d["x"] + 1
"""


# ---------------------------------------------------------
# 7. Key Advantages
# ---------------------------------------------------------

"""
1. Avoids KeyError
2. No need to check if a key exists
3. Cleaner and shorter code
4. Very useful in DSA problems

Common uses:
    - Frequency counting
    - Graph adjacency lists
    - Grouping elements
    - Storing lists of values
"""


# ---------------------------------------------------------
# 8. Quick Comparison
# ---------------------------------------------------------

"""
Normal dict:
    if key not in dict:
        dict[key] = default_value

defaultdict:
    dict[key] automatically gets default value
"""