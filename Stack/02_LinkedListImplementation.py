# Implementation of a Stack using a Singly Linked List in Python

# A stack is a linear data structure that follows the LIFO (Last In First Out) principle.
# This means that the last element added to the stack will be the first one to be removed.
# A stack can be implemented using a singly linked list, where the "top" of the stack is the "head" of the linked list.

# Node Class Definition
class Node:
    def __init__(self, data):
        """
        Initialize a node with the given data.
        
        Args:
            data: The data to be stored in the node.
        """
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node in the list

# Stack Class Definition
class Stack:
    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.head = None  # Top of the stack (head of the linked list)

    def isempty(self):
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self.head == None

    def push(self, data):
        """
        Push a new element onto the stack.
        
        Args:
            data: The data to be pushed onto the stack.
        """
        # Create a new node with the given data
        newnode = Node(data)
        # If the stack is not empty, link the new node to the current head
        if not self.isempty():
            newnode.next = self.head
        # Update the head to the new node
        self.head = newnode

    def pop(self):
        """
        Pop the top element from the stack.
        
        Returns:
            The data of the popped element, or None if the stack is empty.
        """
        # Check if the stack is empty
        if self.isempty():
            return None
        # Store the data of the top node
        poppednode = self.head
        # Move the head to the next node
        self.head = self.head.next
        # Disconnect the popped node from the list
        poppednode.next = None
        # Return the data of the popped node
        return poppednode.data

    def peek(self):
        """
        Return the top element of the stack without removing it.
        
        Returns:
            The data of the top element, or None if the stack is empty.
        """
        # Check if the stack is empty
        if self.isempty():
            return None
        # Return the data of the top node
        return self.head.data

    def display(self):
        """
        Display all elements in the stack.
        """
        # Start from the top of the stack
        iternode = self.head
        # Check if the stack is empty
        if self.isempty():
            print("Stack Underflow")
        else:
            # Traverse the stack and print each element
            while iternode != None:
                print(iternode.data, end="")
                iternode = iternode.next
                if iternode != None:
                    print(" -> ", end="")
            print()

# Driver Code
if __name__ == "__main__":
    # Create a new stack
    MyStack = Stack()

    # Push elements onto the stack
    MyStack.push(11)
    MyStack.push(22)
    MyStack.push(33)
    MyStack.push(44)

    # Display stack elements
    print("Stack elements:")
    MyStack.display()

    # Print the top element of the stack
    print("\nTop element is:", MyStack.peek())

    # Pop elements from the stack
    MyStack.pop()
    MyStack.pop()

    # Display stack elements after popping
    print("\nStack elements after popping twice:")
    MyStack.display()

    # Print the top element of the stack after popping
    print("\nTop element is:", MyStack.peek())

# Explanation of the Concept:
# A stack is a LIFO (Last In First Out) data structure, meaning the last element added is the first one to be removed.
# In this implementation, a singly linked list is used to represent the stack, where the "top" of the stack is the "head" of the linked list.
# - Push Operation: Adds a new element to the top of the stack.
# - Pop Operation: Removes and returns the top element from the stack.
# - Peek Operation: Returns the top element without removing it.
# - Display Operation: Prints all elements in the stack.

# Time Complexity:
# - push(): O(1) - Adding an element to the head of the linked list.
# - pop(): O(1) - Removing the head of the linked list.
# - peek(): O(1) - Accessing the head of the linked list.
# - display(): O(N) - Traversing the entire linked list.

# Space Complexity:
# - O(N) - Where N is the number of elements in the stack.