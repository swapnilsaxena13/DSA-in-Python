"""
Problem: Single Number

Given an array where every element appears twice except one,
find the element that appears only once.

Key Idea:
Use XOR (^) bitwise operation.

XOR Properties:
1. a ^ a = 0        # same numbers cancel out
2. a ^ 0 = a        # XOR with 0 keeps number unchanged
3. XOR is commutative and associative

Because of this:
- numbers appearing twice cancel each other
- the unique number remains

Algorithm:
1. Initialize result = 0
2. XOR every number with result
3. Final result will be the unique number

Time Complexity:  O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            result ^= num   # XOR operation

        return result


# Example
if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]
    print(Solution().singleNumber(nums))  # Output: 4