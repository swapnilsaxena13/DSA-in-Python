# **1. Accessing Keys, Values, and Items in a Dictionary**

# **1.1 Accessing Values using Keys**
dic = {'a': 1, 'b': 2, 'c': 3}
print(dic['a'])  # Output: 1

# 💡 **Note**: If the key doesn't exist, this will raise a `KeyError`. To avoid this, use `.get()`

# ---

# **1.2 Using `.get(key, default_value)`**
print(dic.get('a'))  # Output: 1
print(dic.get('z', 0))  # Output: 0 (since 'z' is not in dic)
# ✅ **Useful when checking for key existence while keeping default values.**

# ---

# **1.3 Accessing All Keys**
print(dic.keys())  # Output: dict_keys(['a', 'b', 'c'])
# ✅ **Converts to a list if needed**:
print(list(dic.keys()))  # Output: ['a', 'b', 'c']

# ---

# **1.4 Accessing All Values**
print(dic.values())  # Output: dict_values([1, 2, 3])
# ✅ **Convert to a list if needed**:
print(list(dic.values()))  # Output: [1, 2, 3]

# ---

# **1.5 Accessing Key-Value Pairs using `.items()`**
for key, value in dic.items():
    print(key, ":", value)
# 🔹 **Output**:
# a : 1
# b : 2
# c : 3
# ✅ **Best way to iterate over dictionaries in most DSA problems.**

# ---

# **2. Modifying a Dictionary**

# **2.1 Adding or Updating Key-Value Pairs**
dic['d'] = 4  # Adding
dic['a'] = 10  # Updating existing key
print(dic)  # Output: {'a': 10, 'b': 2, 'c': 3, 'd': 4}



# **2.2 Checking if a Key Exists**
if 'a' in dic:
    print("Key 'a' exists!")
# ✅ **Avoids KeyError when accessing elements.**

# ---

# **3. Solving DSA Problems Using Dictionaries**

# **3.1 Counting Frequency of Characters in a String**
s = "geeksforgeeks"
dic = {}
for char in s:
    dic[char] = dic.get(char, 0) + 1
print(dic)
# 🔹 **Output**:
# {'g': 2, 'e': 4, 'k': 2, 's': 2, 'f': 1, 'o': 1, 'r': 1}

# ---

# **3.2 Finding First Non-Repeating Character**
# ✅ **Maintaining order while finding first occurrence**
dic = {}
# Step 1: Count frequency
for char in s:
    dic[char] = dic.get(char, 0) + 1
# Step 2: Find first non-repeating character
for char in s:
    if dic[char] == 1:
        print(char)  # Output: f
        break
# 💡 **Iterating over `s` ensures order is maintained.**

# ---

# **3.3 Using `collections.Counter` for Frequency**
from collections import Counter
freq = Counter(s)
print(freq)  # Output: Counter({'e': 4, 'g': 2, 'k': 2, 's': 2, 'f': 1, 'o': 1, 'r': 1})

# ---

# **3.4 Using `defaultdict` for Automatic Key Handling**
from collections import defaultdict
dic = defaultdict(int)
for char in s:
    dic[char] += 1  # No need to check if key exists!
print(dic)  # Output: defaultdict(<class 'int'>, {'g': 2, 'e': 4, 'k': 2, 's': 2, 'f': 1, 'o': 1, 'r': 1})

# ---

# **4. Key Takeaways**
# ✅ Use `dic.get(key, 0)` to **avoid KeyError**.
# ✅ Use `.items()` to iterate over **keys and values** together.
# ✅ Use `defaultdict(int)` if default values are needed.
# ✅ Use `Counter()` for **quick frequency counting**.
# ✅ Always iterate over the **original string (`s`)** if you need order.
