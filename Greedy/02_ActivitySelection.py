# Activity Selection Problem 

"""
Problem Statement:
You are given n activities with their start and finish times.
Select the maximum number of activities that can be performed by a single person,
assuming that a person can only work on a single activity at a time.

Examples:

Input: start[]  =  {10, 12, 20}, finish[] =  {20, 25, 30}
Output: 0 2
Explanation: A person can perform at most two activities. The maximum set of activities that can be executed is {0, 2} [These are indexes in start[] and finish[]]

Input: start[]  =  {1, 3, 0, 5, 8, 5}, finish[] =  {2, 4, 6, 7, 9, 9}
Output: 0 1 3 4
Explanation: A person can perform at most four activities. The maximum set of activities that can be executed is {0, 1, 3, 4} [These are indexes in start[] and finish[]]

Approach:
1. Sort the activities according to their finishing time.
2. Select the first activity from the sorted array.
3. For the remaining activities:
   - If the start time is >= finish time of previously selected activity, select it.

Time Complexity:
- O(N log N) if the activities are not sorted
- O(N) if the activities are already sorted
Auxiliary Space: O(1)
"""

# Implementation: Activity selection assuming activities are sorted by finish time
def printMaxActivities(s, f):
    n = len(f)
    print("The following activities are selected")

    # The first activity is always selected
    i = 0
    print(i, end=" ")

    # Consider rest of the activities
    for j in range(1, n):
        # If start time is >= finish time of last selected
        if s[j] >= f[i]:
            print(j, end=" ")
            i = j

# Driver code
s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
printMaxActivities(s, f)

print("\n")

# More generic implementation - not assuming activities are sorted
def maxactivities(arr):
    n = len(arr)
    arr.sort(key=lambda x: x[1])  # sort by finish time
    prev = 0
    res = 1
    for curr in range(1, n):
        if arr[curr][0] >= arr[prev][1]:
            res += 1
            prev = curr
    return res

# Driver code
arr = [(12, 25), (10, 20), (20, 30)]
print("Max number of activities that can be performed:", maxactivities(arr))
