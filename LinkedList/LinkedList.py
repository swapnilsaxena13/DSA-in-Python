# Node class represents each element of the linked list
class Node:
    def __init__(self, data):
        """
        Initialize a Node.
        :param data: The value to store in this node.
        """
        self.data = data  # Data part of the node
        self.next = None  # Pointer to the next node; initially set to None


# LinkedList class manages the entire linked list
class LinkedList:
    def __init__(self):
        """
        Initialize the LinkedList with no nodes.
        """
        self.head = None  # Head points to the first node in the list. Initially, it's empty (None).

    def append(self, data):
        """
        Add a new node at the end of the linked list.
        :param data: The value to be added to the list.
        """
        new_node = Node(data)  # Create a new node with the given data
        if not self.head:
            # If the list is empty, the new node becomes the head
            self.head = new_node
            return
        # If the list is not empty, traverse to the end
        current = self.head  # Start from the head
        while current.next:  # Move through nodes until you find the last one
            current = current.next
        current.next = new_node  # Link the last node to the new node

    def print_list(self):
        """
        Print all elements in the linked list.
        """
        current = self.head  # Start from the head of the list
        while current:
            # Print the data of the current node and move to the next
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Indicate the end of the list

    def insert_at_beginning(self, data):
        """
        Insert a new node at the beginning of the linked list.
        :param data: The value to be added to the list.
        """
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Point the new node to the current head
        self.head = new_node  # Update the head to be the new node

    def delete_by_value(self, value):
        """
        Delete the first node with the given value.
        :param value: The value of the node to delete.
        """
        # Case 1: The list is empty
        if not self.head:
            print("The list is empty. Nothing to delete.")
            return

        # Case 2: The value is in the head node
        if self.head.data == value:
            self.head = self.head.next  # Update head to the next node
            return

        # Case 3: Traverse the list to find the value
        current = self.head
        while current.next and current.next.data != value:
            current = current.next

        if current.next:  # If the value is found
            current.next = current.next.next  # Skip the node with the given value
        else:
            print(f"Value {value} not found in the list.")

    def search(self, value):
        """
        Search for a value in the linked list.
        :param value: The value to search for.
        :return: True if the value is found, False otherwise.
        """
        current = self.head  # Start from the head
        while current:
            if current.data == value:  # If the value matches, return True
                return True
            current = current.next  # Move to the next node
        return False  # If the loop ends, the value is not found

    def reverse(self):
        """
        Reverse the linked list.
        """
        previous = None  # Initialize the previous node as None
        current = self.head  # Start from the head of the list
        while current:
            next_node = current.next  # Store the next node
            current.next = previous  # Reverse the current node's pointer
            previous = current  # Move the previous node to the current node
            current = next_node  # Move to the next node
        self.head = previous  # Update the head to the new first node


# Demonstration of Linked List Operations
if __name__ == "__main__":
    # Create an empty linked list
    ll = LinkedList()

    # Append elements to the linked list
    ll.append(10)  # Add 10
    ll.append(20)  # Add 20
    ll.append(30)  # Add 30
    print("Linked list after appending elements:")
    ll.print_list()  # Output: 10 -> 20 -> 30 -> None

    # Insert a new element at the beginning
    ll.insert_at_beginning(5)  # Add 5 at the beginning
    print("Linked list after inserting 5 at the beginning:")
    ll.print_list()  # Output: 5 -> 10 -> 20 -> 30 -> None

    # Delete a node by value
    ll.delete_by_value(20)  # Remove 20
    print("Linked list after deleting 20:")
    ll.print_list()  # Output: 5 -> 10 -> 30 -> None

    # Search for a value in the list
    print("Searching for 10 in the list:", ll.search(10))  # Output: True
    print("Searching for 100 in the list:", ll.search(100))  # Output: False

    # Reverse the linked list
    ll.reverse()
    print("Linked list after reversing:")
    ll.print_list()  # Output: 30 -> 10 -> 5 -> None
