from queue import Queue

"""
Core Methods

put(value): Add an element to the rear of the queue.
get(): Remove and return the front element of the queue.
empty(): Check if the queue is empty.
qsize(): Return the current size of the queue.

is threat-safe

"""

class QueueImplementation:
    def __init__(self):
        """
        Initialize the queue using Python's queue.Queue.
        """
        self.queue = Queue()

    def enqueue(self, value):
        """
        Add an element to the rear of the queue.
        :param value: The value to add.
        """
        self.queue.put(value)

    def dequeue(self):
        """
        Remove and return the front element of the queue.
        :return: The front element, or None if the queue is empty.
        """
        if self.queue.empty():
            print("Queue is empty!")
            return None
        return self.queue.get()

    def peek(self):
        """
        View the front element of the queue without removing it.
        Note: `queue.Queue` doesn't have a direct peek method, so this requires additional steps.
        :return: The front element, or None if the queue is empty.
        """
        if self.queue.empty():
            print("Queue is empty!")
            return None
        # To "peek", we need to temporarily dequeue and then re-enqueue the element.
        front = self.queue.get()
        self.queue.put(front)
        for _ in range(self.queue.qsize() - 1):  # Reorder the queue
            self.queue.put(self.queue.get())
        return front

    def isEmpty(self):
        """
        Check if the queue is empty.
        :return: True if empty, False otherwise.
        """
        return self.queue.empty()

    def size(self):
        """
        Get the current size of the queue.
        :return: The number of elements in the queue.
        """
        return self.queue.qsize()
