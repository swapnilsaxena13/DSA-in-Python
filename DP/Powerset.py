"""
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]"""

#Iterative solution

# We will generate the subset by inlitliazing a an empty subset and then starts adding our elements in our empty subset from the nums array in the whole subset one by one.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets=[[]]
        for ele in nums:
            for i in range(len(subsets)):
                subsets.append(subsets[i]+ [ele])
        return subsets


# Recursive solution

#