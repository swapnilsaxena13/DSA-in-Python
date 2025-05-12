
# Importing heapq module to implement a heap queue

import heapq  

# -------------------------------
# Creating a Min-Heap in Python
# -------------------------------
# heapq implements a min-heap, meaning the smallest element is always at index 0
# Using heapify() to convert a list into a heap structure

# Initializing a list
li = [5, 7, 9, 1, 3]

# Converting list into heap using heapify()
heapq.heapify(li)

# Printing created heap
print("The created heap is:", list(li))  # Output: [1, 3, 9, 7, 5]

# -------------------------------
# Pushing and Popping Elements Efficiently
# -------------------------------

# heappush(heap, ele) -> Inserts an element while maintaining the heap order
heapq.heappush(li, 4)  # Pushes 4 into the heap
print("The modified heap after push is:", list(li))  # Output: [1, 3, 4, 7, 5, 9]

# heappop(heap) -> Removes and returns the smallest element from the heap
smallest = heapq.heappop(li)
print("The popped and smallest element is:", smallest)  # Output: 1

# -------------------------------
# Pushing and Popping Simultaneously
# -------------------------------

# heappushpop(heap, ele) -> Pushes an element and then pops the smallest one
li1 = [5, 1, 9, 4, 3]
heapq.heapify(li1)
popped = heapq.heappushpop(li1, 2)  # Push 2, then pop the smallest element
print("The popped item using heappushpop() is:", popped)  # Output: 1

# heapreplace(heap, ele) -> Pops the smallest element, then pushes the new one
li2 = [5, 7, 9, 4, 3]
heapq.heapify(li2)
popped_replace = heapq.heapreplace(li2, 2)
print("The popped item using heapreplace() is:", popped_replace)  # Output: 3

# -------------------------------
# Finding Largest and Smallest Elements
# -------------------------------

# nlargest(k, iterable) -> Returns k largest elements
# nsmallest(k, iterable) -> Returns k smallest elements

li3 = [6, 7, 9, 4, 3, 5, 8, 10, 1]
heapq.heapify(li3)

largest_3 = heapq.nlargest(3, li3)
print("The 3 largest numbers in the list are:", largest_3)  # Output: [10, 9, 8]

smallest_3 = heapq.nsmallest(3, li3)
print("The 3 smallest numbers in the list are:", smallest_3)  # Output: [1, 3, 4]

# --------------------------------------
# Notes:
# 1. heapq creates a min-heap by default. For max-heap, we can use negative values.
# 2. heappushpop() is more efficient than calling heappush() followed by heappop().
# 3. heapreplace() is different from heappushpop() as it always removes the smallest element first.
# 4. nlargest() and nsmallest() do not modify the heap; they just return the required elements.
