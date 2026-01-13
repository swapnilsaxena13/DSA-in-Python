"""
Combination Sum - Backtracking / DFS Notes
------------------------------------------

Problem:
---------
We are given:
1. A list of DISTINCT integers: candidates[]
2. An integer: target

Goal:
-----
Return ALL UNIQUE COMBINATIONS of numbers from candidates such that:
- The chosen numbers sum up to target
- Each number can be used UNLIMITED times
- Order does NOT matter (i.e., combinations, not permutations)

Example:
---------
candidates = [2, 3, 6, 7]
target = 7

Valid combinations:
- [7]
- [2, 2, 3]

Invalid / Duplicate:
- [3, 2, 2] (same as [2,2,3] but in different order → not allowed)


Key Insight:
------------
We want COMBINATIONS, not PERMUTATIONS.

If we generate all possible orders (like [2,3,2] and [3,2,2]), 
we will get duplicates.

To avoid duplicates:
- We process candidates using an INDEX POINTER (i)
- At each step, we make two decisions:
    1) INCLUDE candidates[i]
    2) SKIP candidates[i] and move to i+1
- This ensures:
    * We never go back to earlier elements
    * No duplicate orderings are generated


Decision Tree Idea:
-------------------
At each recursion step, we decide:

1) Include current candidate:
   - Add candidates[i] to current combination
   - Keep i same (because we can reuse the same number)
   - Increase total

2) Skip current candidate:
   - Do NOT add candidates[i]
   - Move index to i+1 (i.e., disallow this number further)

This forms a recursion tree with TWO branches at each step.


Base Cases:
-----------
1) If total == target:
   - Found a valid combination
   - Append a COPY of current combination to result
   - Return

2) If total > target:
   - Cannot continue (all numbers are positive)
   - Return

3) If i >= len(candidates):
   - No more numbers to choose from
   - Return


Why We Use Copy:
----------------
We use ONE list "current" that keeps changing.
When we add a valid combination to result, we must store a COPY:
    result.append(current.copy())
Otherwise, later changes to "current" will corrupt the stored result.


Time Complexity:
----------------
At each step, we branch into two choices (include / skip).

Height of recursion tree ≤ target (because values are positive integers)

Worst Case:
    O(2^T), where T = target

This is exponential, but pruning (total > target) helps in practice.


Implementation (DFS + Backtracking):
------------------------------------
"""

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i: int, current: List[int], total: int):
            # Base Case 1: Found valid combination
            if total == target:
                result.append(current.copy())
                return
            
            # Base Case 2: Exceeded target OR no more candidates
            if total > target or i >= len(candidates):
                return

            # Decision 1: INCLUDE candidates[i]
            current.append(candidates[i])
            dfs(i, current, total + candidates[i])

            # Backtrack (remove last added element)
            current.pop()

            # Decision 2: SKIP candidates[i]
            dfs(i + 1, current, total)

        # Initial call
        dfs(0, [], 0)

        return result


"""
Summary:
--------
- Use backtracking (DFS)
- At each step:
    * Include the number → stay at same index
    * Skip the number → move to next index
- Stop recursion when:
    * total == target → save result
    * total > target → prune
    * index out of bounds → stop
- Guarantees:
    * No duplicate combinations
    * Unlimited reuse of same number
    * Order-independent results

This is a classic "Combination Sum" backtracking pattern.
"""
