from typing import Generic, TypeVar

T = TypeVar('T')

class StaticArray(Generic[T]):
    """
    A type-safe StaticArray class to simulate a fixed-size array with basic operations.
    Provides methods to add, retrieve, set, remove, and print elements while maintaining type safety.
    """

    def __init__(self, capacity: int):
        """
        Constructs a StaticArray with a specified capacity.

        :param capacity: the fixed capacity of the array
        """
        self.capacity = capacity
        self.arr = [None] * capacity  # Initialize the array with None values
        self.length = 0  # Current number of elements

    def add(self, element: T):
        """
        Adds an element at the next open position if there is capacity.

        :param element: the element to be added
        :raises IndexError: if the array is full
        """
        if self.length < self.capacity:
            self.arr[self.length] = element
            self.length += 1
        else:
            raise IndexError("Array is full")

    def get(self, index: int) -> T:
        """
        Returns the element at a specific index.

        :param index: the index of the element to return
        :return: the element at the specified index
        :raises IndexError: if the index is out of range
        """
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range.")
        return self.arr[index]

    def set(self, index: int, element: T):
        """
        Sets a new element at a specific index.

        :param index: the index of the element to replace
        :param element: the element to be stored at the specified position
        :raises IndexError: if the index is out of range
        """
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range.")
        for index in range(self.length -1, index -1, -1):
            self.arr[index + 1] = self.arr[index]
        self.arr[index] = element

    def remove_last(self):
        """
        Removes the last element if the array is not empty.

        :raises IndexError: if the array is empty
        """
        if self.length > 0:
            self.arr[self.length - 1] = None
            self.length -= 1
        else:
            raise IndexError("Array is empty")
        
    """
    Removes element by index and shifts all elements to the left to overwrite the element
    :param index: the index of the element to remove
    """    
        
    def remove_middle(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range.")
        
        # Shift elements to the left starting from the specified index
        for i in range(index, self.length - 1):
            self.arr[i] = self.arr[i + 1]
        
        # Clear the last element and reduce the length
        self.arr[self.length - 1] = None
        self.length -= 1

    def get_length(self) -> int:
        """
        Returns the current number of elements in the array.

        :return: the current number of elements
        """
        return self.length

    def get_capacity(self) -> int:
        """
        Returns the fixed capacity of the array.

        :return: the capacity of the array
        """
        return self.capacity

    def print_array(self):
        """
        Prints all elements in the array up to the current length.
        """
        for i in range(self.length):
            print(self.arr[i], end=" ")
        print()
