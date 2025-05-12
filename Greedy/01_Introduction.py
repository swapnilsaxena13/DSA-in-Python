# Introduction to Greedy Algorithms

"""
Greedy is an algorithmic paradigm that builds up a solution piece by piece,
always choosing the next piece that offers the most obvious and immediate benefit.

Problems best suited for Greedy Algorithms:
- Choosing locally optimal also leads to globally optimal solutions.

Example: Fractional Knapsack Problem
Given a list of items with values and weights, and a Knapsack of capacity W,
choose items (even fractional parts allowed) to maximize total value.

Greedy Strategy:
- Choose the item with the highest value-to-weight ratio first.
- This leads to a global optimum because we can take fractions.

General Property for Greedy Algorithms:
- At every step, make the best choice at that moment.
- This should lead to the optimal solution for the complete problem.

---

Example: Activity Selection Problem

Problem:
Given N activities with their start and finish times,
select the maximum number of activities a single person can do
(only one activity at a time).

Greedy Strategy:
- Always pick the activity that finishes earliest and doesn't overlap.

Steps:
1. Sort activities by finish time.
2. Select the first activity and print it.
3. For each remaining activity:
   - If start time >= finish time of last selected activity, pick it.

Example 1:
start[]  =  {10, 12, 20}
finish[] =  {20, 25, 30}
Output: {0, 2} (two activities)

Example 2:
start[]  =  {1, 3, 0, 5, 8, 5}
finish[] =  {2, 4, 6, 7, 9, 9}
Output: {0, 1, 3, 4} (four activities)

---

Python Example: Minimum Number of Coins

Given a set of coin denominations and an amount,
find the minimum number of coins needed to make that amount using a greedy strategy.
"""

def mincoins(coins, amount):
    coins.sort(reverse=True)  # Sort coins in descending order
    res = 0
    for x in coins:
        if x <= amount:
            c = amount // x
            res += c
            amount -= c * x
        if amount == 0:
            break
    return res

# Example usage
amount = 57
coins = [5, 10, 2, 1]
print(mincoins(coins, amount))  # Output: 7 (10+10+10+10+5+2)
