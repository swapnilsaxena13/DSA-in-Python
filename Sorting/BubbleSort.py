"""
Bubble Sort Algorithm
---------------------
Bubble Sort is the simplest sorting algorithm that works by repeatedly
swapping the adjacent elements if they are in the wrong order.
This algorithm is not suitable for large data sets as its average and
worst-case time complexity is quite high.

How does Bubble Sort Work?

Example:
Input: arr[] = {5, 1, 4, 2, 8}

First Pass:
Bubble sort starts with very first two elements, comparing them to check which one is greater.
(5 1 4 2 8) -> (1 5 4 2 8), Swap since 5 > 1
(1 5 4 2 8) -> (1 4 5 2 8), Swap since 5 > 4
(1 4 5 2 8) -> (1 4 2 5 8), Swap since 5 > 2
(1 4 2 5 8) -> (1 4 2 5 8), No swap since 8 > 5

Second Pass:
(1 4 2 5 8) -> (1 4 2 5 8)
(1 4 2 5 8) -> (1 2 4 5 8), Swap since 4 > 2
(1 2 4 5 8) -> (1 2 4 5 8)
(1 2 4 5 8) -> (1 2 4 5 8)

Third Pass:
Now, the array is already sorted, but the algorithm does not know it.
It needs one whole pass without any swap to confirm sorting.
(1 2 4 5 8) -> (1 2 4 5 8)
(1 2 4 5 8) -> (1 2 4 5 8)
(1 2 4 5 8) -> (1 2 4 5 8)
(1 2 4 5 8) -> (1 2 4 5 8)

---------------------------------------
Bubble Sort Code (Basic Implementation)
---------------------------------------
"""

def bubbleSort_basic(l):
    n = len(l)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]


# Example run
l = [10, 8, 20, 5]
bubbleSort_basic(l)
print("Basic Bubble Sort Output:", *l)  # Output: 5 8 10 20


"""
---------------------------------------
Optimized Bubble Sort
(Stops when list becomes sorted)
---------------------------------------
"""

def bubbleSort_optimized(l):
    n = len(l)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                swapped = True
        if not swapped:
            return


# Example run
l = [10, 8, 20, 5]
bubbleSort_optimized(l)
print("Optimized Bubble Sort Output:", *l)  # Output: 5 8 10 20


"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""
