class ListNode:
    """
    Class representing a single node in a singly linked list.
    """
    def __init__(self, val):
        self.val = val       # Value stored in the node
        self.next = None     # Pointer to the next node


class QueueDummy:
    """
    Class representing a queue implemented using a singly linked list
    with dummy nodes for easier management.
    """
    def __init__(self):
        """
        Initialize the queue with `left` and `right` pointers.
        Both pointers are initially set to None, representing an empty queue.
        """
        self.left = None  # Points to the front of the queue
        self.right = None # Points to the rear of the queue

    def enqueue(self, val):
        """
        Add an element to the end of the queue.
        :param val: The value to be added to the queue.
        """
        newNode = ListNode(val)  # Create a new node with the given value

        if self.right:  # If the queue is not empty
            self.right.next = newNode  # Link the new node to the current rear
            self.right = newNode       # Update the rear pointer to the new node
        else:  # If the queue is empty
            self.left = self.right = newNode  # Both pointers point to the new node

    def dequeue(self):
        """
        Remove and return the front element of the queue.
        :return: The value of the removed element, or None if the queue is empty.
        """
        if not self.left:  # If the queue is empty
            return None

        val = self.left.val  # Store the value of the front node
        self.left = self.left.next  # Move the front pointer to the next node

        if not self.left:  # If the queue is now empty after removal
            self.right = None  # Reset the rear pointer
        return val

    def print(self):
        """
        Print all elements in the queue from front to rear.
        """
        cur = self.left  # Start from the front of the queue
        while cur:
            print(cur.val, ' -> ', end="")  # Print each value followed by an arrow
            cur = cur.next
        print()  # New line after printing all elements

