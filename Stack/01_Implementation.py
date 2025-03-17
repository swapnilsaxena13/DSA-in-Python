# Stack Implementation in Python

# A stack is a linear data structure that follows the Last-In/First-Out (LIFO) principle.
# The main operations are push (insert), pop (remove), and peek (view the top element).

# 1. Stack Implementation using List
stack_list = []

def push_list(item):
    stack_list.append(item)

def pop_list():
    if not is_empty_list():
        return stack_list.pop()
    return None

def peek_list():
    if not is_empty_list():
        return stack_list[-1]
    return None

def is_empty_list():
    return len(stack_list) == 0

def size_list():
    return len(stack_list)

# 2. Stack Implementation using collections.deque
from collections import deque

stack_deque = deque()

def push_deque(item):
    stack_deque.append(item)

def pop_deque():
    if not is_empty_deque():
        return stack_deque.pop()
    return None

def peek_deque():
    if not is_empty_deque():
        return stack_deque[-1]
    return None

def is_empty_deque():
    return len(stack_deque) == 0

def size_deque():
    return len(stack_deque)

# 3. Stack Implementation using queue.LifoQueue
from queue import LifoQueue

stack_queue = LifoQueue()

def push_queue(item):
    stack_queue.put(item)

def pop_queue():
    if not is_empty_queue():
        return stack_queue.get()
    return None

def peek_queue():
    if not is_empty_queue():
        temp = stack_queue.get()
        stack_queue.put(temp)
        return temp
    return None

def is_empty_queue():
    return stack_queue.empty()

def size_queue():
    return stack_queue.qsize()

# 4. Stack Implementation using Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.is_empty():
            popped = self.head.data
            self.head = self.head.next
            return popped
        return None

    def peek(self):
        if not self.is_empty():
            return self.head.data
        return None

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

# Example usage:
if __name__ == "__main__":
    push_list(10)
    push_list(20)
    print(pop_list())  # Output: 20

    push_deque(30)
    push_deque(40)
    print(peek_deque())  # Output: 40

    push_queue(50)
    push_queue(60)
    print(size_queue())  # Output: 2

    ll_stack = LinkedListStack()
    ll_stack.push(70)
    ll_stack.push(80)
    print(ll_stack.pop())  # Output: 80
