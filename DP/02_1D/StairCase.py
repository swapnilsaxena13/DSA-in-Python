"""
Hint 1
If you can advance 2 steps at a time, how many ways can you reach a staircase of height 1 and of height 2? Think recursively.

Hint 2
Continuing from Hint #1, if you know the number of ways to climb a staircase of height 1 and of height 2, how many ways are there to climb a staircase of height 3 (assuming the same max steps of 2)?

Hint 3
The number of ways to climb a staircase of height k with a max number of steps s is:
numWays[k - 1] + numWays[k - 2] + ... + numWays[k - s]
This is because if you can advance between 1 and s steps, then from each step k - 1, k - 2, ..., k - s, you can directly advance to the top of a staircase of height k. By adding the number of ways to reach all steps that you can directly advance to the top step from, you determine how many ways there are to reach the top step.
"""
"""


# Recursive Way of doing this problem
def staircase_traversal(height:int, maxSteps:int):
    if height < 0:
        return 0
    if height == 0:
        return 1
    totalWays=0
    for step in range(1,maxSteps+1):
        totalWays+=staircase_traversal(height-step,maxSteps)
    return totalWays

    
    The time complexity of this code is O(
    """
         
"""
Now, we have to transform this code into a memoized one so for that we will try to store the previous value into a Hashmap(Dictionary) to lower the time complexity """

def staircase_traversal(height:int, maxSteps:int):
    return memoizedCode(height,maxSteps,{})

def memoizedCode(height,maxSteps,map):
    if height in map:
        return map[height]
    if height < 0:
        return 0
    if height == 0:
        return 1
    totalWays=0
    for step in range(1,maxSteps+1):
        totalWays+=memoizedCode(height-step,maxSteps,map)
    return totalWays



# Test Cases
print(staircase_traversal(4, 2))  # Expected Output: 5
print(staircase_traversal(3, 2))  # Expected Output: 3
print(staircase_traversal(8, 2))  # Expected Output: 34
print(staircase_traversal(5, 3))  # Expected Output: 13