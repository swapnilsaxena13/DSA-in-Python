# Dynamic Programming : Climbing Stairs

# Problem Statement:
# Given a number of stairs. Starting from the 0th stair we need to climb to the 
# "Nth" stair. At a time we can climb either one or two steps. We need to return 
# the total number of distinct ways to reach from 0th to Nth stair.

# Pre-req: Recursion, Dynamic Programming Introduction

# How to Identify a DP problem?
# Generally (but not limited to) if the problem statement asks for the following:
# - Count the total number of ways
# - Given multiple ways of doing a task, which way will give the minimum or the maximum output.
# We can try to apply recursion. Once we get the recursive solution, we can go ahead to convert it to a dynamic programming one.

# Steps To Solve The Problem After Identification:
# 1. Try to represent the problem in terms of indexes.
# 2. Try all possible choices/ways at every index according to the problem statement.
# 3. If the question states:
#    - Count all the ways -> return sum of all choices/ways.
#    - Find maximum/minimum -> return the choice/way with maximum/minimum output.

# Using these steps to solve "Climbing Stairs":

# Step 1: We will assume n stairs as indexes from 0 to N.
# Step 2: At a single time, we have 2 choices: Jump one step or jump two steps.
# Step 3: As the problem statement asks to count the total number of distinct ways, 
# we will return the sum of all the choices in our recursive function.

# Base case:
# - When we want to go to the 0th stair, then we have only one option.
# - There will be one more edge-case when n=1, if we call f(n-2) we will reach stair numbered -1 
#   which is not defined, therefore we add an extra test case to return 1 (the only way) when n=1.

# Note:
# If we observe the pseudo-code, it almost matches the problem "fibonacci numbers" discussed in 
# Dynamic Programming Introduction! 

# -------------------------------------------------------------------

# Part 1: Recursive Approach (No Memoization)

def recursive_approach(n):
    # Base cases — the lullabies of recursion
    if n == 0:
        return 1
    if n == 1:
        return 1

    # Two choices: step by 1 or step by 2
    ls = recursive_approach(n-1)
    rs = recursive_approach(n-2)

    # Sum of all paths
    return ls + rs

# Time Complexity: O(2^n) — because of all the overlapping subproblems (brute force)
# Space Complexity: O(N) — because of recursion call stack height

# -------------------------------------------------------------------

# Part 2: Memoized Approach (Top-Down Dynamic Programming)

def memoized_approach(n, dp):
    # Base cases — the anchors of our dreams
    if n == 0:
        return 1
    if n == 1:
        return 1

    if dp[n] != -1:
        return dp[n]  # Already computed, vibe off it

    ls = memoized_approach(n-1, dp)
    rs = memoized_approach(n-2, dp)

    dp[n] = ls + rs  # Save the dream for the future
    return dp[n]

# Time Complexity: O(N)
# Reason: Each state is computed once and then stored.

# Space Complexity: O(N) + O(N)
# Reason: One O(N) for the recursion stack, one O(N) for the dp array.

# -------------------------------------------------------------------

# Part 3: Tabulation Approach (Bottom-Up Dynamic Programming)

def tabulation_approach(n):
    # Setting up the memory to vibe with
    dp = [-1] * (n + 1)
    dp[0] = 1  # 1 way to stay on ground
    dp[1] = 1  # 1 way to reach 1st step

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]  # Building step-by-step, stacking magic

    return dp[n]

# Time Complexity: O(N)
# Space Complexity: O(N)

# -------------------------------------------------------------------

# Part 4: Space Optimized Approach

# Theory behind Space Optimization:
# - If we look closely, to compute dp[i], we only need dp[i-1] and dp[i-2].
# - We don't need to store the entire array — just the *last two values* are enough!
# - Hence, we can compress the space from O(N) to O(1).
# 
# Visualization:
# prev2 -> dp[i-2] (ways to reach two steps back)
# prev  -> dp[i-1] (ways to reach one step back)
# cur_i -> dp[i]   (current ways combining the last two)
# 
# After calculating cur_i, we shift the window:
# prev2 = prev, prev = cur_i
# 
# It's like passing the torch, one runner to the next. 🔥🧑‍🤝‍🧑

def space_optimized_approach(n):
    prev2 = 1  # Ways to reach 0th step
    prev = 1   # Ways to reach 1st step

    for i in range(2, n+1):
        cur_i = prev2 + prev  # Sum of last two
        prev2 = prev          # Move the window forward
        prev = cur_i

    return prev  # Final answer stored in prev

# Time Complexity: O(N)
# Space Complexity: O(1)

# -------------------------------------------------------------------

# Driver code to test all approaches
if __name__ == "__main__":
    n = 3

    print("Recursive Approach Output:", recursive_approach(n))

    dp = [-1] * (n + 1)
    print("Memoized Approach Output:", memoized_approach(n, dp))

    print("Tabulation Approach Output:", tabulation_approach(n))

    print("Space Optimized Approach Output:", space_optimized_approach(n))
