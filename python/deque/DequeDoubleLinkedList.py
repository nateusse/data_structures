class Node:
    """
    Class representing a single node in a doubly linked list.
    """
    def __init__(self, data):
        """
        Initialize a node with data and pointers to previous and next nodes.
        :param data: The value to be stored in the node.
        """
        self.data = data  # The value stored in the node
        self.prev = None  # Pointer to the previous node
        self.next = None  # Pointer to the next node


class DequeDoubleLinkedList:
    """
    Implementation of a Deque (double-ended queue) using a doubly linked list.
    """
    def __init__(self):
        """
        Initialize an empty deque.
        """
        self.head = None  # Pointer to the front of the deque
        self.tail = None  # Pointer to the rear of the deque
        self.size = 0     # Number of elements in the deque

    def append(self, data):
        """
        Add an element to the rear of the deque.
        :param data: The value to be added.
        """
        new_node = Node(data)  # Create a new node
        if not self.head:  # If the deque is empty
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail  # Link the new node to the current tail
            self.tail.next = new_node  # Link the current tail to the new node
            self.tail = new_node       # Update the tail pointer
        self.size += 1  # Increment the size

    def appendleft(self, data):
        """
        Add an element to the front of the deque.
        :param data: The value to be added.
        """
        new_node = Node(data)  # Create a new node
        if not self.head:  # If the deque is empty
            self.head = self.tail = new_node
        else:
            new_node.next = self.head  # Link the new node to the current head
            self.head.prev = new_node  # Link the current head to the new node
            self.head = new_node       # Update the head pointer
        self.size += 1  # Increment the size

    def pop(self):
        """
        Remove and return the element from the rear of the deque.
        :return: The value of the removed element.
        :raises IndexError: If the deque is empty.
        """
        if not self.tail:  # If the deque is empty
            raise IndexError("pop from empty deque")
        data = self.tail.data  # Store the value to be returned
        if self.head == self.tail:  # If there's only one element
            self.head = self.tail = None  # Reset head and tail to None
        else:
            self.tail = self.tail.prev  # Move the tail pointer back
            self.tail.next = None  # Unlink the last node
        self.size -= 1  # Decrement the size
        return data

    def popleft(self):
        """
        Remove and return the element from the front of the deque.
        :return: The value of the removed element.
        :raises IndexError: If the deque is empty.
        """
        if not self.head:  # If the deque is empty
            raise IndexError("pop from empty deque")
        data = self.head.data  # Store the value to be returned
        if self.head == self.tail:  # If there's only one element
            self.head = self.tail = None  # Reset head and tail to None
        else:
            self.head = self.head.next  # Move the head pointer forward
            self.head.prev = None  # Unlink the first node
        self.size -= 1  # Decrement the size
        return data

    def clear(self):
        """
        Remove all elements from the deque.
        """
        self.head = self.tail = None  # Reset head and tail pointers
        self.size = 0  # Reset size

    def __len__(self):
        """
        Return the number of elements in the deque.
        :return: The size of the deque.
        """
        return self.size

    def __iter__(self):
        """
        Iterate over the elements of the deque from front to rear.
        :yield: The data of each node in the deque.
        """
        current = self.head  # Start at the front of the deque
        while current:
            yield current.data  # Yield the value of the current node
            current = current.next  # Move to the next node
