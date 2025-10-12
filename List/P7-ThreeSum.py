"""
Imp.Using Tuples for Removing Duplicates:

Why Tuples:
Tuples are hashable (immutable) and can be added to a set.
Lists are unhashable (mutable) and can't be added to a set.

Process:
Append valid triplets as tuples: (nums[i], nums[st], nums[lt]).
Convert res (list of tuples) to a set to remove duplicates: unique_res = list(set(res)).
Convert tuples back to lists when returning the result: [list(t) for t in unique_res].
"""
"""
Brute Force Approach (O(n³) Time)
This method involves using three nested loops to check all possible triplets in the array. For each combination of three numbers, it calculates their sum and checks if it matches the target. While straightforward, this approach is inefficient for large arrays due to its cubic time complexity.

Optimized Two-Pointer Approach (O(n²) Time)
Sort the Array – This allows efficient traversal using pointers.
Single Loop with Two Pointers –
Fix one number using an outer loop.
Use a left pointer (next to the fixed number) and a right pointer (end of the array).
Adjust pointers based on whether the current sum is less than or greater than the target.
If the sum matches, return the triplet.
Efficiency – Sorting takes O(n log n), and the two-pointer traversal reduces the problem to O(n²), making it significantly faster than brute force.
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array for the two-pointer technique

        res = []
        for i in range(len(nums)):
            st = i + 1  # Left pointer
            lt = len(nums) - 1  # Right pointer
            while st < lt:
                total = nums[i] + nums[st] + nums[lt]
                if total == 0 and i != st and i != lt and st != lt:
                    # Append the triplet as a tuple to help remove duplicates using a set
                    res.append((nums[i], nums[st], nums[lt]))
                    st += 1
                    lt -= 1
                elif total < 0:
                    st += 1
                else:
                    lt -= 1

        # Remove duplicates using a set and convert tuples back to lists
        unique_res = list(map(list, set(res)))
        return unique_res


# Example usage
if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]  # Example input
    solution = Solution()
    result = solution.threeSum(nums)
    print(result)
