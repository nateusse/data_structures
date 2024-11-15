class DequeWithStacks:
    """
    Implementation of a deque using two stacks.
    """
    def __init__(self):
        """
        Initialize two stacks to simulate deque operations.
        """
        self.stack_front = []  # Stack for the front of the deque
        self.stack_rear = []   # Stack for the rear of the deque

    def _transfer(self, source, destination):
        """
        Transfer all elements from one stack to another.
        :param source: The stack to transfer elements from.
        :param destination: The stack to transfer elements to.
        """
        while source: #while len(sfront) > 1
            destination.append(source.pop()) #append back

    def append(self, value):
        """
        Add an element to the rear of the deque.
        :param value: The value to add.
        """
        self.stack_rear.append(value)

    def appendleft(self, value):
        """
        Add an element to the front of the deque.
        :param value: The value to add.
        """
        self.stack_front.append(value)

    def pop(self):
        """
        Remove and return the element from the rear of the deque.
        :return: The value of the removed element, or None if the deque is empty.
        """
        if not self.stack_rear:  # If the rear stack is empty
            if not self.stack_front:  # If both stacks are empty
                raise IndexError("pop from an empty deque")
            self._transfer(self.stack_front, self.stack_rear)  # Transfer elements to rear stack
        return self.stack_rear.pop()

    def popleft(self):
        """
        Remove and return the element from the front of the deque.
        :return: The value of the removed element, or None if the deque is empty.
        """
        if not self.stack_front:  # If the front stack is empty
            if not self.stack_rear:  # If both stacks are empty
                print("Deque is empty!")
                return None
            self._transfer(self.stack_rear, self.stack_front)  # Transfer elements to front stack
        return self.stack_front.pop()

    def isEmpty(self):
        """
        Check if the deque is empty.
        :return: True if the deque is empty, False otherwise.
        """
        return not self.stack_front and not self.stack_rear

    def getSize(self):
        """
        Get the current size of the deque.
        :return: The number of elements in the deque.
        """
        return len(self.stack_front) + len(self.stack_rear)

    def printDeque(self):
        """
        Print all elements in the deque.
        """
        # Print in the correct order: elements in stack_front (reversed) + stack_rear
        front = list(reversed(self.stack_front))
        rear = self.stack_rear
        print("Deque:", front + rear)

    def count(self, x):
        """Count the number of deque elements equal to x."""
        return self.front_stack.count(x) + self.back_stack.count(x)
    
    def extend(self, iterable):
        """Extend the right side of the deque with elements from the iterable."""
        for item in iterable:
            self.append(item)
    

    def __len__(self):
        """Return the number of elements in the deque."""
        return len(self.front_stack) + len(self.back_stack)
    
    def __bool__(self):
        """Return True if the deque has elements, False otherwise."""
        return bool(self.front_stack or self.back_stack)
    
    def __iter__(self):
        """Return an iterator over the deque's elements from left to right."""
        yield from reversed(self.front_stack)
        yield from self.back_stack