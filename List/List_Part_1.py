# Python script demonstrating various list operations
"""
Demonstrating List Operations in Python:
1. append() - Adds an element to the end of the list.
2. insert() - Inserts an element at a specific position in the list.
3. del - Deletes an element at a specific index (does not return it).
4. pop() - Removes an element at a specific index (or last by default) and returns it.
5. remove() - Removes the first occurrence of a specified value from the list.
6. sort() - Sorts a list permanently.
7. sorted() - Sorts a list temporarily.
8. reverse() - Reverses the order of the list.
9. len() - Finds the number of elements in the list.
"""

# initialize an empty list 
list = []


# Accessing Elements in a List
print("### Accessing Elements in a List ###")
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print("First bicycle:", bicycles[0])  # Accessing the first element

# Using Individual Values from a List
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
print()

# Modifying Elements in a List
print("### Modifying Elements in a List ###")
motorcycles = ['honda', 'yamaha', 'suzuki']
print("Original list:", motorcycles)
motorcycles[0] = 'ducati'  # Modifying the first element
print("Modified list:", motorcycles)
print()

# Appending Elements to the End of a List
print("### Appending Elements to a List ###")
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')  # Adding an element at the end
print("List after appending:", motorcycles)
print()

# Inserting Elements into a List
print("### Inserting Elements into a List ###")
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')  # Adding 'ducati' at index 0
print("List after insertion:", motorcycles)
print()

# Removing an Item Using the del Statement
print("### Removing an Item Using del Statement ###")
motorcycles = ['honda', 'yamaha', 'suzuki']
print("Original list:", motorcycles)
del motorcycles[0]  # Deletes the first element by index
print("List after deletion:", motorcycles)
# Use case: Use `del` when you know the index and don't need the removed value.
print()

# Removing an Item Using the pop() Method
print("### Removing an Item Using pop() Method ###")
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()  # Removes and returns the last element by default
print("List after popping:", motorcycles)
print("Popped motorcycle:", popped_motorcycle)
# Use case: Use `pop()` when you need to retrieve the removed item.
print()

# Popping Items from Any Position
print("### Popping Items from Any Position ###")
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)  # Removes and retrieves the first element
print(f"The first motorcycle I owned was a {first_owned.title()}.")
print()

# Removing an Item by Value
print("### Removing an Item by Value ###")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')  # Removes the first occurrence of 'ducati'
print("List after removal:", motorcycles)
# Use case: Use `remove()` when you know the value but not the index.
# Note: It raises an error if the value is not in the list.
print()

# Sorting a List Permanently with the sort() Method
print("### Sorting a List Permanently ###")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()  # Sorts the list permanently
print("Sorted list:", cars)
print()

# Sorting a List Temporarily with sorted() Function
print("### Sorting a List Temporarily ###")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Original list:", cars)
print("Temporarily sorted list:", sorted(cars))  # Sorting temporarily
print("Original list remains unchanged:", cars)
print()

# Printing a List in Reverse Order
print("### Printing a List in Reverse Order ###")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()  # Reverses the list order
print("Reversed list:", cars)
print()

# Finding the Length of a List
print("### Finding the Length of a List ###")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Number of cars in the list:", len(cars))
print()
