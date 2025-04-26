"""
Dynamic Programming Introduction

Dynamic Programming (DP) is a technique to store answers to sub-problems and reuse them later to solve the main problem efficiently.

Two common DP approaches:
1. Memoization (Top-Down): Solve the main problem first, then break it down to base cases.
2. Tabulation (Bottom-Up): Solve base cases first, then build up to the main problem.

Example: Fibonacci Series (0, 1, 1, 2, 3, 5, 8, ...)
Recurrence Relation: fib(n) = fib(n-1) + fib(n-2), where fib(0) = 0, fib(1) = 1.
"""

# Part 1: Memoization (Top-Down Approach)
def fib_memoization(n, dp):
    """
    Memoization: Store computed results to avoid redundant calculations.
    Steps:
    1. Initialize dp array with -1.
    2. Check if solution exists in dp before computing.
    3. Store computed results in dp before returning.
    
    Time Complexity: O(N) - Each subproblem solved once.
    Space Complexity: O(N) - Recursion stack + dp array.
    """
    if n <= 1:
        return n
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib_memoization(n-1, dp) + fib_memoization(n-2, dp)
    return dp[n]

# Part 2: Tabulation (Bottom-Up Approach)
def fib_tabulation(n):
    """
    Tabulation: Iteratively solve from base cases to main problem.
    Steps:
    1. Initialize dp array with base cases (dp[0] = 0, dp[1] = 1).
    2. Iterate from 2 to n, filling dp using recurrence relation.
    
    Time Complexity: O(N) - Simple loop.
    Space Complexity: O(N) - dp array.
    """
    dp = [-1] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# Part 3: Space Optimization
def fib_space_optimized(n):
    """
    Space Optimization: Use variables instead of dp array since only last two values are needed.
    Steps:
    1. Track prev (fib(i-1)) and prev2 (fib(i-2)).
    2. Update cur_i, prev2, and prev iteratively.
    
    Time Complexity: O(N) - Simple loop.
    Space Complexity: O(1) - Constant space.
    """
    if n <= 1:
        return n
    prev2, prev = 0, 1
    for _ in range(2, n + 1):
        cur_i = prev2 + prev
        prev2 = prev
        prev = cur_i
    return prev

if __name__ == "__main__":
    n = 5
    # Memoization
    dp = [-1] * (n + 1)
    print(f"Fibonacci (Memoization): {fib_memoization(n, dp)}")  # Output: 5
    
    # Tabulation
    print(f"Fibonacci (Tabulation): {fib_tabulation(n)}")  # Output: 5
    
    # Space Optimized
    print(f"Fibonacci (Space Optimized): {fib_space_optimized(n)}")  # Output: 5