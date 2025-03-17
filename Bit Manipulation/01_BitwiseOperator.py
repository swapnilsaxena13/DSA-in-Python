
#Bitwise Operators and Algorithms in Python

## Overview
"""
Bitwise operations are used to manipulate bits efficiently.
These operations are much faster and can optimize certain computational tasks.


## List of Bitwise Operators
1. **Bitwise AND (&)** - Returns 1 if both bits are 1, else 0.
2. **Bitwise OR (|)** - Returns 1 if either bit is 1, else 0.
3. **Bitwise XOR (^)** - Returns 1 if one bit is 1 and the other is 0.
4. **Bitwise NOT (~)** - Inverts all bits.
5. **Bitwise Right Shift (>>) ** - Shifts bits to the right (equivalent to integer division by powers of 2).
6. **Bitwise Left Shift (<<) ** - Shifts bits to the left (equivalent to integer multiplication by powers of 2).

## Important Facts about Bitwise Operators
- Left and right shift operators cannot be used with negative numbers.
- The XOR (^) operator is particularly useful in technical interviews.
- Bitwise operators should not replace logical operators.
- AND (&) can be used to check if a number is even or odd (x & 1 == 0 → even, x & 1 == 1 → odd).

## Bitwise Operations Implementation

"""
# Bitwise AND
x = 5  # 101 in binary
y = 3  # 011 in binary
print("Bitwise AND (5 & 3):", x & y)  # Output: 1 (001 in binary)

# Bitwise OR
print("Bitwise OR (5 | 3):", x | y)  # Output: 7 (111 in binary)

# Bitwise XOR
print("Bitwise XOR (5 ^ 3):", x ^ y)  # Output: 6 (110 in binary)

# Bitwise NOT
print("Bitwise NOT (~5):", ~x)  # Output: -6 (Two's complement)

# Bitwise Shift Operations
print("Right shift (10 >> 1):", 10 >> 1)  # Output: 5
print("Left shift (10 << 1):", 10 << 1)  # Output: 20

## Bitwise Algorithms

### Setting a Bit
# To set a bit at nth position, use OR operator:
def set_bit(num, n):
    return num | (1 << n)

### Unsetting a Bit
# To unset a bit at nth position, use AND with NOT operator:
def unset_bit(num, n):
    return num & ~(1 << n)

### Toggling a Bit
# To toggle a bit at nth position, use XOR operator:
def toggle_bit(num, n):
    return num ^ (1 << n)

### Checking if a Bit is Set
# To check if nth bit is set, use AND operator:
def check_bit(num, n):
    return (num & (1 << n)) != 0

### Divide by 2 using Bitwise Right Shift
# Equivalent to num // 2
print("Divide by 2 (18 >> 1):", 18 >> 1)  # Output: 9

### Multiply by 2 using Bitwise Left Shift
# Equivalent to num * 2
print("Multiply by 2 (18 << 1):", 18 << 1)  # Output: 36

### Finding Log Base 2
# log2(x) can be found by counting shifts until x becomes zero:
def log2(x):
    res = 0
    while x >> 1:
        x >>= 1
        res += 1
    return res

### Swapping Two Numbers using XOR
# Swaps two numbers without using temporary variable:
def swap(a, b):
    a ^= b
    b ^= a
    a ^= b
    return a, b

### Check if a Number is Power of 2
# A number is a power of 2 if N & (N - 1) == 0

def is_power_of_2(n):
    return (n & (n - 1)) == 0 and n != 0

### Find Most Significant Bit (MSB)
def most_significant_bit(n):
    return 1 << (n.bit_length() - 1)

### XOR of All Numbers from 1 to N
def xor_1_to_n(n):
    rem = n % 4
    if rem == 0:
        return n
    elif rem == 1:
        return 1
    elif rem == 2:
        return n + 1
    else:
        return 0

### Maximum AND Value in an Array
def max_and(arr):
    res = 0
    for bit in range(31, -1, -1):
        count = sum(1 for num in arr if (num & (res | (1 << bit))) == (res | (1 << bit)))
        if count >= 2:
            res |= (1 << bit)
    return res


