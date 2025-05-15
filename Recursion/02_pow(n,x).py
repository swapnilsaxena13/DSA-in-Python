class Solution:

    """
    ❌ Version 1: Linear Recursion (Inefficient)

    🔁 Linear Recursion Approach:
The linear recursion version of myPow(x, n) calculates x^n by multiplying x recursively n times, reducing n by 1 in each recursive call. It has a simple base case when n == 0, returning 1. However, this approach has two major flaws: it does not handle negative exponents, and its time complexity is O(n), which makes it inefficient for large values of n due to deep recursion and high memory usage.
    """

    def myPow_linear(self, x: float, n: int) -> float:
        # ⚠️ Mistake 1: No handling for negative n
        if n == 0:
            return 1
        power = self.myPow_linear(x, n - 1)
        return x * power
    
    """
    ✅ Version 2: Optimized (Exponentiation by Squaring)
    
⚡ Optimized Exponentiation by Squaring Approach:
The optimized version improves performance by using Exponentiation by Squaring, which reduces the problem size by half in each step. It first handles the case when n is negative by inverting x and converting n to positive. Then, it recursively computes myPow(x, n//2), squares the result, and multiplies by x once more if n is odd. This reduces the time complexity to O(log n), making it much more efficient and scalable for large inputs.
    """
    
    def myPow_optimized(self, x: float, n: int) -> float:
        # ✅ Base case
        if n == 0:
            return 1
        
        # ✅ Fix for negative powers
        if n < 0:
            x = 1 / x
            n = -n
        
        half = self.myPow_optimized(x, n // 2)
        res = half * half
        
        # ✅ If n is odd, multiply once more by x
        if n % 2 == 1:
            res *= x
        return res


# 🔍 Test Cases
s = Solution()

print("Linear Version:")
try:
    print("myPow_linear(2, 3) =", s.myPow_linear(2, 3))  # ✅ Works
    print("myPow_linear(2, -2) =", s.myPow_linear(2, -2))  # ❌ Will cause infinite recursion
except RecursionError:
    print("RecursionError: myPow_linear(2, -2) failed due to unhandled negative exponent")

print("\nOptimized Version:")
print("myPow_optimized(2, 3) =", s.myPow_optimized(2, 3))  # ✅ 8
print("myPow_optimized(2, -2) =", s.myPow_optimized(2, -2))  # ✅ 0.25
print("myPow_optimized(3, 0) =", s.myPow_optimized(3, 0))  # ✅ 1

# 🔍 Mistakes Summary (as comments):
"""
🔴 Common Mistakes Identified:
1. ❌ No handling of negative exponents → leads to infinite recursion.
2. ❌ In linear recursion, repeated calls cause O(n) stack depth → slow and memory-heavy.
3. ❌ Using / instead of // in recursion step would cause float input and non-terminating recursion.
4. ✅ Optimized version uses:
   - base case n == 0
   - handles negative n early
   - uses integer division (//)
   - reduces time complexity to O(log n)

✅ Best Practice:
Always handle edge cases (like negative numbers) before diving into recursion or loops.
"""