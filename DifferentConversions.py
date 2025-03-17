"""
🚀 Summary of Most Useful Conversions with Examples
-----------------------------------------------------
This script provides a quick reference for common type conversions in Python, along with
examples to illustrate how each conversion works.
"""

# ------------------------------------------
# 🚀 Summary of Most Useful Conversions
# ------------------------------------------
# | Conversion                        | Method                                    | Example Input              | Expected Output     |
# |----------------------------------|-------------------------------------------|----------------------------|---------------------|
# | List → String                   | "".join(lst)                              | ['H', 'e', 'l', 'l', 'o']  | 'Hello'             |
# | String → List                   | list(s)                                   | "Hello"                    | ['H', 'e', 'l', 'l', 'o'] |
# | Integer → String                | str(num)                                  | 123                        | '123'               |
# | String → Integer                | int(s)                                    | "123"                      | 123                 |
# | List → Integer                  | int("".join(map(str, lst)))               | [1, 2, 3]                  | 123                 |
# | Integer → List (digits)         | list(map(int, str(num)))                  | 123                        | [1, 2, 3]           |
# | List of Integers → List of Strings | list(map(str, lst))                      | [1, 2, 3]                  | ['1', '2', '3']     |
# | Tuple → List                     | list(tup)                                 | (1, 2, 3)                  | [1, 2, 3]           |
# | List → Tuple                     | tuple(lst)                                | [1, 2, 3]                  | (1, 2, 3)           |
# | Dictionary Keys → List           | list(d.keys())                            | {'a': 1, 'b': 2}           | ['a', 'b']          |
# | Dictionary Values → List         | list(d.values())                          | {'a': 1, 'b': 2}           | [1, 2]              |
# | Set → List                       | list(s)                                   | {1, 2, 3}                  | [1, 2, 3]           |
# | List → Set (Remove Duplicates)   | set(lst)                                  | [1, 2, 2, 3]               | {1, 2, 3}           |
# | Binary → Decimal                 | int(bin_str, 2)                           | "1010"                     | 10                  |
# | Decimal → Binary                 | bin(num)[2:]                              | 10                         | '1010'              |
# | Hexadecimal → Decimal            | int(hex_str, 16)                          | "A"                        | 10                  |
# | Decimal → Hexadecimal            | hex(num)[2:]                              | 10                         | 'a'                 |
# | Octal → Decimal                  | int(oct_str, 8)                           | "12"                       | 10                  |
# | Decimal → Octal                  | oct(num)[2:]                              | 10                         | '12'                |
# | Character → ASCII                | ord(char)                                 | 'A'                        | 65                  |
# | ASCII → Character                | chr(num)                                  | 65                         | 'A'                 |

# 🔥 **Useful Tricks:**
# - Use `map()` for efficient type conversions on iterables.
# - Use `''.join()` for fast string concatenation from lists.
# - Use `set()` to remove duplicates from lists quickly.
# - Convert lists to dictionaries using `dict(zip(keys, values))`.
# - Convert list of tuples to dictionary using `dict(lst_of_tuples)`.
