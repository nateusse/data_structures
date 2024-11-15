from collections import deque

class QueueCollectionDeque:
    def __init__(self):
        self.queue = deque()  # Deque is the underlying data structure

    def enqueue(self, value):
        self.queue.append(value)  # Add to the rear

    def dequeue(self):
        if not self.queue:
            raise IndexError("Queue is empty!")
        return self.queue.popleft()  # Remove from the front

    def peek(self):
        if not self.queue:
            raise IndexError("Queue is empty!")
        return self.queue[0]  # View the front element

    def isEmpty(self):
        return not self.queue

    def size(self):
        return len(self.queue)
