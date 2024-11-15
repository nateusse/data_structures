class ListNode:
    """
    Class representing a single node in the linked list.
    """
    def __init__(self, value):
        self.value = value  # Value of the node
        self.next = None    # Pointer to the next node


"""
Queue implemented using a linked list
- Enqueue: (last node) O(1)
- Dequeue: (first node) O(1)
- Peek: (first node) O(1)


"""


class QueueLinkedList:
    """
    Queue implementation using a linked list.
    """
    def __init__(self):
        """
        Initialize the queue with pointers to the front and rear.
        """
        self.front = None  # Points to the front of the queue
        self.rear = None   # Points to the rear of the queue
        self.size = 0      # Tracks the size of the queue

    def enqueue(self, value):
        """
        Add an element to the rear of the queue.
        :param value: The value to add.
        """
        new_node = ListNode(value)  # Create a new node
        if not self.rear:  # If the queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node  # Link the new node to the rear
            self.rear = new_node       # Update the rear pointer
        self.size += 1

    def dequeue(self):
        """
        Remove and return the front element of the queue.
        :return: The front element, or None if the queue is empty.
        """
        if not self.front:  # If the queue is empty
            print("Queue is empty!")
            return None
        value = self.front.value  # Get the value of the front node
        self.front = self.front.next  # Move the front pointer to the next node
        if not self.front:  # If the queue becomes empty
            self.rear = None  # Update the rear pointer
        self.size -= 1
        return value

    def peek(self):
        """
        View the front element of the queue without removing it.
        :return: The front element, or None if the queue is empty.
        """
        if not self.front:
            print("Queue is empty!")
            return None
        return self.front.value

    def isEmpty(self):
        """
        Check if the queue is empty.
        :return: True if empty, False otherwise.
        """
        return self.front is None

    def getSize(self):
        """
        Get the current size of the queue.
        :return: The size of the queue.
        """
        return self.size

    def printQueue(self):
        """
        Print all elements in the queue from front to rear.
        """
        current = self.front
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print() #new line

