# Fractional Knapsack Problem - Notes and Implementation

# Problem:
# Given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
# In Fractional Knapsack, we can break items to maximize the total value.

# Example Input:
# arr = [(60, 10), (100, 20), (120, 30)]
# W = 50
# Output: Maximum possible value = 240
# Explanation: Take items with weight 10, 20 and 2/3 of 30 kg item

# Greedy Approach:
# 1. Calculate value/weight ratio for each item
# 2. Sort all items in decreasing order of ratio
# 3. Initialize result = 0, current capacity = W
# 4. For every item in sorted order:
#    - If item can be picked completely, pick it
#    - Else pick fraction of it and break

# Time Complexity: O(N log N) due to sorting
# Space Complexity: O(N)

# Class to represent an item
class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

# Function to calculate value/weight ratio
def compare(item):
    return item.value / item.weight

# Greedy function to solve the Fractional Knapsack problem
def fractional_knapsack(W, arr):
    # Sorting items by value/weight ratio in descending order
    arr.sort(key=compare, reverse=True)

    final_value = 0.0  # Result

    for item in arr:
        if item.weight <= W:
            W -= item.weight
            final_value += item.value
        else:
            final_value += item.value * (W / item.weight)
            break

    return final_value

# Example usage
if __name__ == "__main__":
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    W = 50
    max_value = fractional_knapsack(W, arr)
    print(f"Maximum value we can obtain = {max_value}")

    arr2 = [Item(500, 30)]
    W2 = 10
    max_value2 = fractional_knapsack(W2, arr2)
    print(f"Maximum value we can obtain = {max_value2:.3f}")
