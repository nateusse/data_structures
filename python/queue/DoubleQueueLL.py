class Node:
    """
    Class representing a node in a doubly linked list.
    """
    def __init__(self, value):
        self.value = value  # Value stored in the node
        self.next = None    # Pointer to the next node
        self.prev = None    # Pointer to the previous node


class DoubleQueueLL:
    """
    Double-Ended Queue (Deque) implementation using a doubly linked list (without dummy nodes).
    """
    def __init__(self):
        """
        Initialize the deque with head and tail pointers.
        """
        self.head = None  # Points to the front of the deque
        self.tail = None  # Points to the rear of the deque
        self.size = 0     # Tracks the number of elements in the deque

    def append(self, value):
        """
        Add an element to the rear of the deque.
        :param value: The value to add.
        """
        new_node = Node(value)
        if not self.tail:  # If the deque is empty
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def appendleft(self, value):
        """
        Add an element to the front of the deque.
        :param value: The value to add.
        """
        new_node = Node(value)
        if not self.head:  # If the deque is empty
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def pop(self):
        """
        Remove and return the element from the rear of the deque.
        :return: The value of the removed element, or None if the deque is empty.
        """
        if not self.tail:  # If the deque is empty
            print("Deque is empty!")
            return None
        value = self.tail.value
        if self.head == self.tail:  # If there is only one element
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1
        return value

    def popleft(self):
        """
        Remove and return the element from the front of the deque.
        :return: The value of the removed element, or None if the deque is empty.
        """
        if not self.head:  # If the deque is empty
            print("Deque is empty!")
            return None
        value = self.head.value
        if self.head == self.tail:  # If there is only one element
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return value

    def isEmpty(self):
        """
        Check if the deque is empty.
        :return: True if the deque is empty, False otherwise.
        """
        return self.size == 0

    def getSize(self):
        """
        Get the current size of the deque.
        :return: The number of elements in the deque.
        """
        return self.size

    def printDeque(self):
        """
        Print all elements in the deque from front to rear.
        """
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

