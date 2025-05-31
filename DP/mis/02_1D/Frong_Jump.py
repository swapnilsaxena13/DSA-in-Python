#############################################
# Dynamic Programming: Frog Jump (DP 3)    #
#############################################

"""
Problem Statement:
-------------------
Given a number of stairs and a frog, the frog wants to climb from the 0th stair to the (N-1)th stair.
At a time, the frog can climb either one or two steps.
A height[N] array is given.
Whenever the frog jumps from stair i to stair j, the energy consumed is abs(height[i] - height[j]).
Goal: Return the **minimum energy** used to jump from stair 0 to stair N-1.

Example:
---------
Input: height = [30, 10, 60, 10, 60, 50]
Output: 40
"""

# ------------------------------------------------------------
# Important Thought: Why NOT Greedy?
# ------------------------------------------------------------
"""
Taking the locally minimum jump every time might not lead to a globally minimum path.
Greedy could trap you into a path that seems cheap but becomes expensive later.
So, Dynamic Programming to the rescue! 🚀
"""

# ------------------------------------------------------------
# Step 1: Define Subproblem
# ------------------------------------------------------------
"""
Let f(i) = minimum energy required to reach stair i.
So, f(0) = 0 (base case)
"""

# ------------------------------------------------------------
# Step 2: Choices
# ------------------------------------------------------------
"""
From any stair `i`, frog can:
 - Jump 1 step back: (i-1)
 - Jump 2 steps back: (i-2)

Cost = abs(height[i] - height[i-1]) or abs(height[i] - height[i-2])
"""

# ------------------------------------------------------------
# Step 3: Recurrence Relation
# ------------------------------------------------------------
"""
At any stair `i`:
f(i) = min(
        f(i-1) + abs(height[i] - height[i-1]),
        f(i-2) + abs(height[i] - height[i-2])
      )
"""

# ------------------------------------------------------------
# Memoization (Top-Down Recursive DP)
# ------------------------------------------------------------
import sys
import math

def solve(ind, height, dp):
    if ind == 0:
        return 0
    if dp[ind] != -1:
        return dp[ind]

    jumpOne = solve(ind-1, height, dp) + abs(height[ind] - height[ind-1])
    jumpTwo = sys.maxsize
    if ind > 1:
        jumpTwo = solve(ind-2, height, dp) + abs(height[ind] - height[ind-2])

    dp[ind] = min(jumpOne, jumpTwo)
    return dp[ind]

if __name__ == "__main__":
    height = [30, 10, 60, 10, 60, 50]
    n = len(height)
    dp = [-1] * n
    print("Minimum Energy (Memoization):", solve(n-1, height, dp))

"""
Complexity:
- Time: O(N)
- Space: O(N) (for recursion + dp array)
"""

# ------------------------------------------------------------
# Tabulation (Bottom-Up Iterative DP)
# ------------------------------------------------------------

def tabulation_main():
    height = [30, 10, 60, 10, 60, 50]
    n = len(height)
    dp = [-1 for _ in range(n)]
    dp[0] = 0

    for ind in range(1, n):
        jumpOne = dp[ind-1] + abs(height[ind]-height[ind-1])
        jumpTwo = float('inf')
        if ind > 1:
            jumpTwo = dp[ind-2] + abs(height[ind]-height[ind-2])
        dp[ind] = min(jumpOne, jumpTwo)

    print("Minimum Energy (Tabulation):", dp[n-1])

if __name__ == "__main__":
    tabulation_main()

"""
Complexity:
- Time: O(N)
- Space: O(N)
"""

# ------------------------------------------------------------
# Space Optimized Approach
# ------------------------------------------------------------

def optimized_main():
    height = [30, 10, 60, 10, 60, 50]
    n = len(height)
    prev = 0
    prev2 = 0

    for i in range(1, n):
        jumpOne = prev + abs(height[i] - height[i - 1])
        jumpTwo = sys.maxsize
        if i > 1:
            jumpTwo = prev2 + abs(height[i] - height[i - 2])

        cur_i = min(jumpOne, jumpTwo)
        prev2 = prev
        prev = cur_i

    print("Minimum Energy (Space Optimized):", prev)

if __name__ == "__main__":
    optimized_main()

"""
Complexity:
- Time: O(N)
- Space: O(1) <- NO external dp array! 🔥
"""

# ---------------------- END OF NOTES ----------------------
# 🌟 Keep Grinding! DP is pure magic once you feel it! 🌟
