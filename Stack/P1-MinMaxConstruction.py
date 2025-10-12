"""
Stores all values in a single stack. To get the minimum, it scans the whole stack 
— making getMin() an O(n) operation.	

Tracks min and max at every push using an extra stack. This lets getMin() and getMax() run in O(1) time 
— faster, smarter, more efficient.

"""
# -------------------------------
# MinStack Implementation (Basic)
# -------------------------------

class MinStack:
    def __init__(self):
        # O(1) time | O(1) space
        self.stack = []

    def push(self, val):
        # O(1) time | O(1) space
        self.stack.append(val)

    def pop(self):
        # O(1) time | O(1) space
        self.stack.pop()

    def top(self):
        # O(1) time | O(1) space
        return self.stack[-1]

    def getMin(self):
        # O(n) time | O(1) space
        return min(self.stack)


# ---------------------------------
# MinMaxStack Implementation (Advanced)
# ---------------------------------

class MinMaxStack:
    def __init__(self):
        # O(1) time | O(1) space
        self.minMaxStack = []
        self.stack = []

    def peek(self):
        # O(1) time | O(1) space
        return self.stack[len(self.stack) - 1]

    def pop(self):
        # O(1) time | O(1) space
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        # O(1) time | O(1) space
        newMinMax = {"min": number, "max": number}
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax["min"] = min(lastMinMax["min"], number)
            newMinMax["max"] = max(lastMinMax["max"], number)
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)

    def getMin(self):
        # O(1) time | O(1) space
        return self.minMaxStack[len(self.minMaxStack) - 1]["min"]

    def getMax(self):
        # O(1) time | O(1) space
        return self.minMaxStack[len(self.minMaxStack) - 1]["max"]


# -----------------------------
# Test / Demo Code Starts Here
# -----------------------------

if __name__ == "__main__":
    print("=== Testing MinStack ===")
    ms = MinStack()
    ms.push(3)
    ms.push(5)
    ms.push(2)
    ms.push(1)
    print("Top:", ms.top())        # Should be 1
    print("Min:", ms.getMin())     # Should be 1
    ms.pop()
    print("Top after pop:", ms.top())   # Should be 2
    print("Min after pop:", ms.getMin()) # Should be 2

    print("\n=== Testing MinMaxStack ===")
    mms = MinMaxStack()
    mms.push(3)
    mms.push(5)
    mms.push(2)
    mms.push(1)
    print("Top:", mms.peek())        # Should be 1
    print("Min:", mms.getMin())      # Should be 1
    print("Max:", mms.getMax())      # Should be 5
    mms.pop()
    print("Top after pop:", mms.peek())   # Should be 2
    print("Min after pop:", mms.getMin()) # Should be 2
    print("Max after pop:", mms.getMax()) # Should be 5
