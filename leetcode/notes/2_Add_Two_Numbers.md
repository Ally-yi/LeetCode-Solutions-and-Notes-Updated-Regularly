# Add Two Numbers (LeetCode #2)

**Problem Link:** [https://leetcode.com/problems/add-two-numbers/](https://leetcode.com/problems/add-two-numbers/)

# Linked List and List (Array) Knowledge Explanation

## 1. Basic Definitions

### 1.1 List (Array)
- A data structure that stores elements in a contiguous block of memory.
- Supports fast random access by index.
- Inserting or deleting elements (except at the end) requires shifting elements.

### 1.2 Linked List
- A linked list is a linear data structure made up of a sequence of nodes, where each node contains data and a pointer to the next node.
- Simple diagram:
![ListNode in a Linked List](https://media.geeksforgeeks.org/wp-content/uploads/20220712172013/Singlelinkedlist.png)


## 2. Comparison Table

| Feature           | List (Array)               | Linked List                 |
|-------------------|----------------------------|----------------------------|
| Storage           | Contiguous memory          | Non-contiguous nodes linked via pointers |
| Access Speed      | Fast, direct indexing O(1) | Slow, sequential access O(n) |
| Insertion/Deletion| Slow, requires shifting O(n) | Fast, pointer manipulation O(1) |
| Memory Usage      | Fixed size or resizing overhead | Dynamic, flexible size allocation |
| Use Cases         | Frequent reads, fixed size | Frequent insertions/deletions |



## 3. Code

### 3.1 List (Array) Example

```python
# Create a list (array)
my_list = [1, 2, 3, 4, 5]

# Access an element by index
print(my_list[2])  # Output: 3

# Insert element at index 2
my_list.insert(2, 99)  
print(my_list)  # Output: [1, 2, 99, 3, 4, 5]

# Remove element at index 3
my_list.pop(3)  
print(my_list)  # Output: [1, 2, 99, 4, 5]
```
### 3.2 Linked List Example
```
# Define a node in a linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val        # Store node's value
        self.next = next      # Reference to the next node

# Define the singly linked list
class LinkedList:
    def __init__(self):
        self.head = None      # Initialize empty list with no head node

    def append(self, val):
        new_node = ListNode(val)  # Create a new node
        if not self.head:
            self.head = new_node  # If list is empty, new node becomes head
            return
        current = self.head
        while current.next:
            current = current.next  # Traverse to the last node
        current.next = new_node      # Append the new node at the end

    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")  # Print node value
            current = current.next            # Move to next node
        print("None")

# Testing the linked list
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()  # Output: 1 -> 2 -> 3 -> None
```
### 3.3 List ↔ Linked List Example
```python
# Define a node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val        # Value of the node
        self.next = next      # Pointer to the next node

# Define LinkedList with append and print functionality
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        """Append a new node to the end of the list."""
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Print the linked list from head to tail."""
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

# Convert a Python list to a linked list
def list_to_linkedlist(lst):
    """Convert a Python list to a linked list (return head node)."""
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Convert a linked list to a Python list
def linkedlist_to_list(node):
    """Convert a linked list to a Python list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# Convert list → linked list
nums = [10, 20, 30]
head = list_to_linkedlist(nums)

# Print linked list manually
print("Manual linked list from list:")
current = head
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")  # Output: 10 -> 20 -> 30 -> None

# Convert linked list → list
arr = linkedlist_to_list(head)
print("Back to Python list:", arr)  # Output: [10, 20, 30]

# Using LinkedList class
print("Using LinkedList class:")
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.print_list()  # Output: 1 -> 2 -> 3 -> None
```
## 4. Summary

- **List (Array)**: Best for random access and static data size.
- **Singly Linked List**: Ideal when frequent insertions/deletions are needed and you don’t require indexing.
- Conversion functions make it easy to work between formats in testing and practical code.