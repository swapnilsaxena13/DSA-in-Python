"""
Problem Statement:
You are given a non-empty array of positive integers representing the execution times of queries. Only one query can be executed at a time, but the order can be chosen. The waiting time for a query is the sum of the execution times of all queries executed before it. The goal is to determine the minimum total waiting time for all queries.

Example:
For queries [1, 4, 5], if executed in the order [5, 1, 4], the total waiting time is calculated as:

First query (5): waits 0 → total += 0
Second query (1): waits 5 → total += 5
Third query (4): waits 5 + 1 = 6 → total += 6
Total waiting time = 0 + 5 + 6 = 11.

Sample Input:
queries = [3, 2, 1, 2, 6]

Sample Output:
17

Hints Provided:
Determine the optimal order of execution to minimize total waiting time.

Consider sorting the array in place to solve the problem efficiently.

Sort the array and execute the shortest queries first.

Calculate the total waiting time by iterating through the sorted array, adding the product of the remaining queries and the current query's duration at each step.
"""

def minimumWaitingTime(queries):
    queries.sort()
    waiting_time=0
    arr=[]
    for i in range(0,len(queries)-1):
        waiting_time+=queries[i]
        arr.append(waiting_time)
    return sum(arr)





#Sample Input 1
queries1 = [3, 2, 1, 2, 6]
print("Input:", queries1)
print("Output:", minimumWaitingTime(queries1))  # Expected: 17

# Sample Input 2
queries2 = [1, 4, 5]
print("\nInput:", queries2)
print("Output:", minimumWaitingTime(queries2))  # Expected: 6

# Sample Input 3 (Single query)
queries3 = [5]
print("\nInput:", queries3)
print("Output:", minimumWaitingTime(queries3))  # Expected: 0

# Sample Input 4 (All same durations)
queries4 = [1, 1, 1, 1, 1]
print("\nInput:", queries4)
print("Output:", minimumWaitingTime(queries4))  # Expected: 10