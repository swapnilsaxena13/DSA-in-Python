"""
Selection Sort Algorithm
------------------------
The selection sort algorithm sorts an array by repeatedly finding
the minimum element (considering ascending order) from the unsorted
part and putting it at the beginning.

The algorithm maintains two subarrays:
1) The subarray which is already sorted.
2) Remaining subarray which is unsorted.

In every iteration, the minimum element from the unsorted subarray
is picked and moved to the sorted subarray.

-------------------------------------------------
How Selection Sort Works (Example)
-------------------------------------------------
Consider arr[] = {64, 25, 12, 22, 11}

First Pass:
Traverse the array [64, 25, 12, 22, 11].
Minimum element = 11. Swap with 64.
Array after 1st pass: [11, 25, 12, 22, 64]

Second Pass:
Now traverse remaining [25, 12, 22, 64].
Minimum element = 12. Swap with 25.
Array after 2nd pass: [11, 12, 25, 22, 64]

Third Pass:
Now traverse remaining [25, 22, 64].
Minimum element = 22. Swap with 25.
Array after 3rd pass: [11, 12, 22, 25, 64]

Fourth Pass:
Now traverse remaining [25, 64].
Minimum element = 25. Already in correct position.
Array after 4th pass: [11, 12, 22, 25, 64]

Fifth Pass:
Last element (64) is already the largest, stays at the end.
Final Sorted Array: [11, 12, 22, 25, 64]

-------------------------------------------------
Selection Sort Code
-------------------------------------------------
"""

def selectSort(l):
    n = len(l)
    for i in range(n - 1):
        min_ind = i
        for j in range(i + 1, n):
            if l[j] < l[min_ind]:
                min_ind = j
        # Swap the found minimum element with the first element
        l[min_ind], l[i] = l[i], l[min_ind]


# Example run
l = [10, 5, 8, 20, 2, 18]
selectSort(l)
print("Selection Sort Output:", *l)  # Output: 2 5 8 10 18 20


"""
Time Complexity: O(n^2)  (for all cases)
Best Case: O(n^2)
Worst Case: O(n^2)
Average Case: O(n^2)

Space Complexity: O(1)  (In-place sorting)
"""
