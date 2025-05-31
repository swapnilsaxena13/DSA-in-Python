# ---------------- Problem Statement ----------------
# Given two strings s1 and s2, find the length of their Longest Common Subsequence (LCS).
# A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
# For example:
# s1 = "AGGTAB"
# s2 = "GXTXAYB"
# The LCS is "GTAB", so the answer is 4.

s1 = "AGGTAB"
s2 = "GXTXAYB"
n1 = len(s1)
n2 = len(s2)

# ---------------- Recursive Code of LCS ----------------
# Pure recursive approach without memoization
# Time Complexity: O(2^n), very inefficient for large inputs
def lcsRecur(s1: str, s2: str, n1: int, n2: int) -> int:
    # Base condition: if any string is exhausted, return 0
    if n1 == 0 or n2 == 0:
        return 0
    # If last characters match, reduce both lengths
    elif s1[n1 - 1] == s2[n2 - 1]:
        return 1 + lcsRecur(s1, s2, n1 - 1, n2 - 1)
    else:
        # Otherwise, find the max by reducing one string at a time
        return max(lcsRecur(s1, s2, n1, n2 - 1), lcsRecur(s1, s2, n1 - 1, n2))

# ---------------- Memoized (Top-Down) Code of LCS ----------------
# Memoization avoids recalculating overlapping subproblems
# Time Complexity: O(n1 * n2)
# Space Complexity: O(n1 * n2) for the DP table

# Create DP table with -1, indicating uncomputed states
dp = [[-1 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

def lcsMemo(s1: str, s2: str, n1: int, n2: int) -> int:
    # Check if already computed
    if dp[n1][n2] != -1:
        return dp[n1][n2]
    
    # Base condition
    if n1 == 0 or n2 == 0:
        dp[n1][n2] = 0
    elif s1[n1 - 1] == s2[n2 - 1]:
        # If characters match, take diagonal value + 1
        dp[n1][n2] = 1 + lcsMemo(s1, s2, n1 - 1, n2 - 1)
    else:
        # If characters don't match, take max of left and top cell
        dp[n1][n2] = max(lcsMemo(s1, s2, n1, n2 - 1), lcsMemo(s1, s2, n1 - 1, n2))
    
    return dp[n1][n2]

# ---------------- Tabulation (Bottom-Up) Code of LCS ----------------
# Iterative version using 2D DP table
# Time Complexity: O(n1 * n2)
# Space Complexity: O(n1 * n2)

def lcs(x, y):
    m = len(x)
    n = len(y)

    # Initialize a 2D dp table filled with 0
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill the table in bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                # Characters match, so take diagonal value + 1
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                # Characters don't match, take max from left or top
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Final result is in bottom-right cell
    return dp[m][n]

# ---------------- Run & Output ----------------
# You can call any of the three versions

result = lcsMemo(s1, s2, n1, n2)
print("Length of Longest Common Subsequence:", result)

# You can test the other two like this:
# print("Recursive Result:", lcsRecur(s1, s2, n1, n2))
# print("Tabulation Result:", lcs(s1, s2))
