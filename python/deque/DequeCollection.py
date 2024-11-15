from collections import deque

"""
Abstract data type, implemented using a deque collections.
Methods are:
- append(value): 
- appendleft(value): 
- pop(): 
- popleft(): 
- isEmpty(): 
OTHER METHODS
   count(x): Count occurrance of x
   index(x, start, stop): Firt index of x
   insert(i, x): Insert x at i


"""


class DequeCollection:
    """
    A wrapper class around collections.deque to demonstrate deque operations.
    """
    def __init__(self):
        """
        Initialize an empty deque.
        """
        self.deque = deque()

    def append(self, value):
        """
        Add an element to the rear of the deque.
        :param value: The value to add.
        """
        self.deque.append(value)

    def appendleft(self, value):
        """
        Add an element to the front of the deque.
        :param value: The value to add.
        """
        self.deque.appendleft(value)

    def pop(self):
        """
        Remove and return the element from the rear of the deque.
        :return: The value of the removed element.
        """
        if self.isEmpty():
            print("Deque is empty!")
            return None
        return self.deque.pop()

    def popleft(self):
        """
        Remove and return the element from the front of the deque.
        :return: The value of the removed element.
        """
        if self.isEmpty():
            print("Deque is empty!")
            return None
        return self.deque.popleft()

    def isEmpty(self):
        """
        Check if the deque is empty.
        :return: True if empty, False otherwise.
        """
        return len(self.deque) == 0

    def count(self, x):
        """
        Count the occurrences of an element in the deque.
        :param x: The element to count.
        :return: The number of occurrences of x.
        """
        return self.deque.count(x)

    def index(self, x, start=0, stop=None):
        """
        Find the first occurrence of x in the deque between start and stop.
        :param x: The element to find.
        :param start: The starting index for the search.
        :param stop: The ending index for the search.
        :return: The index of the first occurrence of x.
        """
        if stop is None:
            stop = len(self.deque)
        try:
            return self.deque.index(x, start, stop)
        except ValueError:
            print(f"{x} not found in deque.")
            return -1

    def insert(self, i, x):
        """
        Insert an element x at index i.
        :param i: The index where the element should be inserted.
        :param x: The element to insert.
        """
        self.deque.insert(i, x)

    def printDeque(self):
        """
        Print all elements in the deque.
        """
        print("Deque:", list(self.deque))

