"""Hint 1

The Binary Search algorithm works by finding the number in the middle of the input array and comparing it to the target number. Given that the array is sorted, if this middle number is smaller than the target number, then the entire left part of the array is no longer worth exploring since the target number can no longer be in it; similarly, if the middle number is greater than the target number, then the entire right part of the array is no longer worth exploring. Applying this logic recursively eliminates half of the array until the number is found or until the array runs out of numbers.

Hint 2

Write a helper function that takes in two additional arguments: a left pointer and a right pointer representing the indices at the extremities of the array (or subarray) that you are applying Binary Search on. The first time this helper function is called, the left pointer should be zero and the right pointer should be the final index of the input array. To find the index of the middle number mentioned in Hint #1, simply round down the number obtained from: (left + right) / 2. Apply this logic recursively until you find the target number or until the left pointer becomes greater than the right pointer.

Hint 3

Can you implement this algorithm iteratively? Are there any advantages to doing so?"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort once
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid  # return index of target
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


# -----------------------------
# Example usage (test cases)
# -----------------------------
if __name__ == "__main__":
    nums = [5, 2, 9, 1, 7, 3]
    target = 7

    sol = Solution()
    result = sol.search(nums, target)

    print(f"Array after sorting: {sorted(nums)}")
    print(f"Target {target} found at index: {result}")
