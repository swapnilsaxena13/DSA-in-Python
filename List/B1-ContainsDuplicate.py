"""
217. Contains Duplicate - Explanation
Problem Link: https://leetcode.com/problems/contains-duplicate/description/

Description
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false

"""

"""
Brute Force :
At first we will look at the number  in array [1,2,3,3] that is 1 we will look for this number wheater this has appeared in the list again if yes we will return true otherwise we will look for the second number that is 2 wheather this number is there in the list or not.
Time complexity: O(n^2)
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(0,len(nums)):         

            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False
"""  
Mistake 1 (First Code):
You used
for i in nums:
    for j in range(i+1, len(nums)):
❌ Problem: i is a value, not an index — using it inside range() is wrong.
"""


"""
By Sorting we can reduce the time complexity. As this array [1,2,3,1] will become [1,1,2,3] so now we have to only look for the adjacent elements rather than the whole to check whether is their any duplicate in the array or not.
Time complexity: O(nlog(n))
Space complexity: O(1) or O(n) depending on the sorting algorithm as sorting algorithm takes extra space.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                    return True
        return False
        
"""
If we dont have constraints about space then we can use Hash set as we will start storing our elements in hash set and check while storing the next element as it is there in the hash set or not if it is there then return true else false. 

"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen= set()
        for i in range(0,len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
            elif nums[i] in seen:
                return True
        return False
        

"""
We can also use the length of the hash set if there is a duplicate element in the array then the lenght of the hash set will be less than the lenght of our array.
"""




