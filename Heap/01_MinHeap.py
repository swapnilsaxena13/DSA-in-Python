import math

class myMinHeap:
    def __init__(self):
        """
        Initialize an empty min heap using a list.
        The heap follows the property where the parent node is always smaller than its child nodes.
        """
        self.arr = []  # List to store heap elements

    def parent(self, i):
        """
        Returns the index of the parent node of the given index i.
        Formula: (i - 1) // 2
        """
        return (i - 1) // 2

    def lChild(self, i):
        """
        Returns the index of the left child of node at index i.
        Formula: 2 * i + 1
        """
        return 2 * i + 1

    def rChild(self, i):
        """
        Returns the index of the right child of node at index i.
        Formula: 2 * i + 2
        """
        return 2 * i + 2

    def insert(self, x):
        """
        Inserts a new element into the heap while maintaining the min-heap property.
        Steps:
        1. Append the new element at the end of the heap.
        2. Compare with its parent and swap if the parent is greater.
        3. Repeat step 2 until the heap property is restored.
        """
        arr = self.arr
        arr.append(x)  # Insert at the end
        i = len(arr) - 1  # Index of the newly inserted element

        # Bubble up the new element to maintain the heap property
        while i > 0 and arr[self.parent(i)] > arr[i]:
            p = self.parent(i)
            arr[i], arr[p] = arr[p], arr[i]  # Swap with parent
            i = p  # Move up to parent index

    def minHeapify(self, i):
        """
        Maintains the min-heap property by ensuring the node at index i is smaller than its children.
        Steps:
        1. Compare node i with its left and right children.
        2. Swap with the smallest child if necessary.
        3. Recursively apply the function to the affected subtree.
        """
        arr = self.arr
        lt = self.lChild(i)
        rt = self.rChild(i)
        smallest = i
        n = len(arr)

        if lt < n and arr[lt] < arr[smallest]:
            smallest = lt
        if rt < n and arr[rt] < arr[smallest]:
            smallest = rt

        if smallest != i:
            arr[smallest], arr[i] = arr[i], arr[smallest]  # Swap
            self.minHeapify(smallest)  # Recursively heapify the affected subtree

    def extractMin(self):
        """
        Removes and returns the smallest element (root) from the heap.
        Steps:
        1. Swap the root with the last element.
        2. Remove the last element (previous root).
        3. Call minHeapify(0) to restore heap property.
        """
        arr = self.arr
        n = len(arr)

        if n == 0:
            return math.inf  # Heap is empty, return infinity
        res = arr[0]  # Root element (minimum value)

        arr[0] = arr[n - 1]  # Move last element to root
        arr.pop()  # Remove last element

        self.minHeapify(0)  # Restore heap property
        return res

    def decreaseKey(self, i, x):
        """
        Decreases the value of a node at index i and ensures heap property is maintained.
        Steps:
        1. Update value at index i.
        2. Bubble up the new value to its correct position.
        """
        arr = self.arr
        arr[i] = x

        while i != 0 and arr[self.parent(i)] > arr[i]:
            p = self.parent(i)
            arr[i], arr[p] = arr[p], arr[i]  # Swap
            i = p  # Move up

    def delete(self, i):
        """
        Deletes a node at index i from the heap.
        Steps:
        1. Replace the value with negative infinity (-inf).
        2. Move it to the root by bubbling up.
        3. Extract the minimum element to remove it completely.
        """
        n = len(self.arr)
        if i >= n:
            return  # Index out of bounds
        
        self.decreaseKey(i, -math.inf)  # Set to negative infinity and bubble up
        self.extractMin()  # Remove the root (minimum value)

# Test the heap implementation
if __name__ == "__main__":
    heap = myMinHeap()
    heap.insert(10)
    heap.insert(5)
    heap.insert(20)
    heap.insert(2)
    heap.insert(8)
    
    print("Heap after inserts:", heap.arr)
    print("Extracted min:", heap.extractMin())
    print("Heap after extracting min:", heap.arr)
    heap.decreaseKey(2, 1)
    print("Heap after decreasing key at index 2 to 1:", heap.arr)
    heap.delete(1)
    print("Heap after deleting index 1:", heap.arr)

