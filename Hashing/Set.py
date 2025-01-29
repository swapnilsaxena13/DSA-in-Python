# Python Sets - Overview and Operations

# A Set is an unordered, iterable, mutable, and hash-based collection that has no duplicate elements.
# It is represented using curly braces `{}` or the set() constructor.

# Note: Sets are unordered, so items cannot be accessed using an index.
#       Operations like membership testing and union are optimized using a hash table.

# --- Set Creation ---
print("--- Set Creation ---")
s1 = {10, 20, 30}  # Set with curly braces
print("s1:", s1)

s2 = set([20, 30, 40])  # Set using set() constructor
print("s2:", s2)

s3 = {}  # This creates a dictionary, NOT a set
print("Type of s3:", type(s3))

s4 = set()  # Empty set
print("Type of s4:", type(s4))
print("s4:", s4)

# --- Adding Elements to a Set ---
print("\n--- Adding Elements to a Set ---")
s = {10, 20}
s.add(30)  # Adds a single element
print("After add(30):", s)
s.add(30)  # Adding duplicate, set remains unchanged
print("After adding duplicate 30:", s)

s.update([40, 50])  # Adds multiple elements
print("After update([40, 50]):", s)

s.update([60, 70], [80, 90])  # Adds elements from multiple iterables
print("After multiple updates:", s)

# --- Removing Elements from a Set ---
print("\n--- Removing Elements from a Set ---")
s = {10, 20, 30, 40}
s.discard(30)  # Removes an element if present, no error if not found
print("After discard(30):", s)
s.remove(20)  # Removes an element, raises KeyError if not found
print("After remove(20):", s)
s.clear()  # Empties the set
print("After clear():", s)
s.add(50)  # Adding an element to empty set
print("After add(50):", s)
del s  # Deletes the set completely

# --- Set Operations ---
print("\n--- Set Operations ---")
s1 = {2, 4, 6, 8}
s2 = {3, 6, 9}

# Union: Combines elements from both sets, removes duplicates
print("Union:", s1 | s2)
print("Union (method):", s1.union(s2))

# Intersection: Common elements between sets
print("Intersection:", s1 & s2)
print("Intersection (method):", s1.intersection(s2))

# Difference: Elements in s1 but not in s2
print("Difference:", s1 - s2)
print("Difference (method):", s1.difference(s2))

# Symmetric Difference: Elements not common to both sets
print("Symmetric Difference:", s1 ^ s2)


# --- Set Relationship Operations ---
print("\n--- Set Relationship Operations ---")
s1 = {2, 4, 6, 8}
s2 = {4, 8}

# Disjoint: Checks if two sets have no common elements
print("Disjoint Sets:", s1.isdisjoint(s2))

# Subset: Checks if s2 is a subset of s1
print("Is Subset (<=):", s1 <= s2)
print("Is Subset (method):", s1.issubset(s2))

# Proper Subset: Checks if s2 is a proper subset of s1
print("Is Proper Subset (<):", s1 < s2)

# Superset: Checks if s1 is a superset of s2
print("Is Superset (>=):", s1 >= s2)
print("Is Superset (method):", s1.issuperset(s2))

# Proper Superset: Checks if s1 is a proper superset of s2
print("Is Proper Superset (>):", s1 > s2)

# --- Notes ---
# 1. Use `add()` to add a single element, `update()` for multiple elements.
# 2. `remove()` raises an error if the element is missing, while `discard()` does not.
# 3. Sets are unordered, so do not rely on order of elements.
# 4. Use `isdisjoint()`, `issubset()`, and `issuperset()` for relationship checks.
# 5. Operations like union, intersection, and difference work efficiently due to hash tables.
