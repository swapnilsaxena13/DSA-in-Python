"""198. House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 """

"""
**Your approach (Dynamic Programming):**

1. Handle base cases:

   * No houses → return 0
   * One house → return its value
2. Initialize an array `maxSums` as a copy of `nums` to store the max loot up to each house.
3. Iterate from the 3rd house onward (`i = 2` to `len(nums)-1`):

   * At each house, choose the maximum between:

     * Skipping this house → `maxSums[i-1]`
     * Robbing this house → `maxSums[i-2] + nums[i]`
4. Return `maxSums[-1]` as the result.

"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        maxSums=nums[:]
        maxSums[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            maxSums[i]=max(maxSums[i-1],maxSums[i-2]+nums[i]) 
        return maxSums[-1]
        