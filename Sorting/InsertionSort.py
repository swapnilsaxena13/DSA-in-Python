"""
Insertion Sort Algorithm
------------------------
Insertion sort is a simple sorting algorithm that works similar
to the way you sort playing cards in your hands. The array is 
virtually split into a sorted and an unsorted part. Values from
the unsorted part are picked and placed at the correct position
in the sorted part.

Example:
---------
Consider arr[] = {12, 11, 13, 5, 6}

Working of Insertion Sort:

First Pass:
Initially, compare the first two elements (12 and 11).
12 > 11, so they are not in order. Swap them.
Now sorted sub-array = {11, 12}.
Array: [11, 12, 13, 5, 6]

Second Pass:
Compare 12 and 13.
Since 13 > 12, no swap needed.
Sorted sub-array = {11, 12, 13}.
Array: [11, 12, 13, 5, 6]

Third Pass:
Next element is 5.
Compare 13 and 5 → swap → [11, 12, 5, 13, 6]
Compare 12 and 5 → swap → [11, 5, 12, 13, 6]
Compare 11 and 5 → swap → [5, 11, 12, 13, 6]
Now 5 is in the correct position.
Array: [5, 11, 12, 13, 6]

Fourth Pass:
Next element is 6.
Compare 13 and 6 → swap → [5, 11, 12, 6, 13]
Compare 12 and 6 → swap → [5, 11, 6, 12, 13]
Compare 11 and 6 → swap → [5, 6, 11, 12, 13]
Now 6 is in the correct position.
Final Array: [5, 6, 11, 12, 13]

---------------------------------------
Insertion Sort Algorithm (Code)
---------------------------------------
"""

def insertionSort(l):
    for i in range(1, len(l)):
        x = l[i]
        j = i - 1

        # Shift elements greater than x to one position ahead
        while j >= 0 and x < l[j]:
            l[j + 1] = l[j]
            j = j - 1
        l[j + 1] = x


# Example run
l = [20, 5, 40, 60, 10, 30]
insertionSort(l)
print("Insertion Sort Output:", *l)  # Output: 5 10 20 30 40 60


"""
Time Complexity: O(n^2)
Best Case (Already Sorted): O(n)
Worst Case: O(n^2)
Average Case: O(n^2)

Space Complexity: O(1)  (In-place sorting)
"""
