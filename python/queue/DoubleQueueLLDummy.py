"""

Design a Double-ended Queue class.

Your Deque class should support the following operations:

Deque() will initialize an empty queue.
bool isEmpty() will return whether the queue is empty or not.
void append(int value) will insert value at the end of the queue.
void appendleft(int val) will insert value at the beginning of the queue.
int pop() will remove and return the value at the end of the queue. 
If the queue is empty, return -1.
int popleft() will remove and return the value at the beginning of the queue.
 If the queue is empty, return -1.

Note: You should implement each operation in O(1)O(1) time complexity
"""

class ListNode:
    """
    Class representing a node in a doubly linked list.
    """
    def __init__(self, value):
        self.value = value  # Value stored in the node
        self.next = None    # Pointer to the next node
        self.prev = None    # Pointer to the previous node


class DoubleQueueLLDummy:
    """
    Double-Ended Queue (Deque) implementation using a doubly linked list.
    """
    def __init__(self):
        """
        Initialize the deque with dummy head and tail nodes.
        """
        self.head = ListNode(-1)  # Dummy head node
        self.tail = ListNode(-1)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def append(self, value):
        """
        Add an element to the rear of the deque.
        :param value: The value to add.
        """
        new_node = ListNode(value)
        last_node = self.tail.prev

        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.tail
        self.tail.prev = new_node

        self.size += 1

    def appendleft(self, value):
        """
        Add an element to the front of the deque.
        :param value: The value to add.
        """
        new_node = ListNode(value)
        first_node = self.head.next

        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = first_node
        first_node.prev = new_node

        self.size += 1

    def pop(self):
        """
        Remove and return the element from the rear of the deque.
        :return: The value of the removed element, or None if the deque is empty.
        """
        if self.isEmpty():
            print("Deque is empty!")
            return None

        last_node = self.tail.prev
        value = last_node.value
        second_last_node = last_node.prev

        second_last_node.next = self.tail
        self.tail.prev = second_last_node

        self.size -= 1
        return value

    def popleft(self):
        """
        Remove and return the element from the front of the deque.
        :return: The value of the removed element, or None if the deque is empty.
        """
        if self.isEmpty():
            print("Deque is empty!")
            return None

        first_node = self.head.next
        value = first_node.value
        second_node = first_node.next

        self.head.next = second_node
        second_node.prev = self.head

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
        current = self.head.next
        while current != self.tail:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

