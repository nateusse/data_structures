class Stack:
    """
    A simple stack implementation using a Python list.
    """

    def __init__(self):
        """
        Initializes an empty stack.
        """
        self.stack = []

    def push(self, item):
        """
        Pushes an item onto the stack.

        :param item: The item to push onto the stack.
        """
        self.stack.append(item)

    def pop(self):
        """
        Removes and returns the top item from the stack.

        :return: The top item from the stack.
        :raises IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.stack.pop()

    def peek(self):
        """
        Returns the top item of the stack without removing it.

        :return: The top item of the stack.
        :raises IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.stack[-1]

    def is_empty(self):
        """
        Checks if the stack is empty.

        :return: True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0

    def size(self):
        """
        Returns the number of items in the stack.

        :return: The size of the stack.
        """
        return len(self.stack)

    def print_stack(self):
        """
        Prints the elements of the stack.
        """
        print(self.stack)
