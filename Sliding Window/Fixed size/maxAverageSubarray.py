
# Problem: Find the maximum average of any contiguous subarray of size k

# Approach:
# 1. Use a sliding window of size k to avoid recomputing sums repeatedly.
# 2. Initialize the sum of the first k elements.
# 3. Slide the window one index at a time:
#     - Subtract the element leaving the window.
#     - Add the new element entering the window.
# 4. Track the maximum sum seen.
# 5. Return the maximum sum divided by k for the average.


def findMaxAverage(nums: List[int], k: int) -> float:
    # Step 1: Calculate the initial window sum of size k
    sum_of_num = sum(nums[0:k])
    left = 0
    right = k - 1
    curr_sum = sum_of_num

    # Step 2: Slide the window one element at a time
    while right < len(nums) - 1:
        right += 1
        left += 1
        # Proper sliding window: remove leftmost, add rightmost
        curr_sum = curr_sum + nums[right] - nums[left - 1]
        sum_of_num = max(curr_sum, sum_of_num)

    # Step 3: Return the maximum average
    return sum_of_num / k


# Test cases
nums1 = [4, 2, 1, 3, 3]
k1 = 2
print("Maximum average of subarrays of length", k1, "is:", findMaxAverage(nums1, k1))  # Expected: 3.0

nums2 = [1, 12, -5, -6, 50, 3]
k2 = 4
print("Maximum average of subarrays of length", k2, "is:", findMaxAverage(nums2, k2))  # Expected: 12.75

nums3 = [5]
k3 = 1
print("Maximum average of subarrays of length", k3, "is:", findMaxAverage(nums3, k3))  # Expected: 5.0

nums4 = [0, 4, 0, 3, 2]
k4 = 1
print("Maximum average of subarrays of length", k4, "is:", findMaxAverage(nums4, k4))  # Expected: 4.0

nums5 = [-1, -2, -3, -4, -5]
k5 = 3
print("Maximum average of subarrays of length", k5, "is:", findMaxAverage(nums5, k5))  # Expected: -2.0



# 1. You reused the initial sum (`sum_of_num`) inside the loop instead of updating the sliding window sum.
#    → You wrote: curr_sum = sum_of_num + nums[right] - nums[left - 1]
#    → This causes accumulation errors because the window is not sliding correctly.

# 2. You initialized and reused `sum_of_num` as both the sliding sum and the max value,
#    leading to confusion and logic bugs.

# 3. You added a special case check `if k == 1:` — which was unnecessary if the sliding window logic was correct.
#    → The general logic works fine for k = 1.
