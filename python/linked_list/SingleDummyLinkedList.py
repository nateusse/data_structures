class ListNode:
    """
    Class representing a node in a singly linked list.
    """
    def __init__(self, val: int):
        self.val = val       # The value stored in the node
        self.next = None     # Pointer to the next node in the list


class SingleDummyLinkedList:
    """
    Class representing a singly linked list with basic operations.
    """
    def __init__(self):
        """
        Initialize the linked list with a dummy head node.
        Using a dummy node simplifies operations like removal 
        at the beginning of the list.
        """
        self.head = ListNode(-1)  # Dummy head node
        self.tail = self.head     # Tail points to the dummy node initially

    def insertEnd(self, val: int):
        """
        Insert a new node with the given value at the end of the linked list.
        :param val: The value to be added to the list.
        """
        new_node = ListNode(val)   # Create a new node
        self.tail.next = new_node  # Link the new node at the end of the list
        self.tail = new_node       # Update the tail pointer

    def remove(self, index: int):
        """
        Remove the node at the specified index.
        :param index: The position of the node to remove (0-based index).
        """
        i = 0
        curr = self.head  # Start from the dummy head node

        # Traverse to the node just before the target index
        while i < index and curr.next:
            i += 1
            curr = curr.next

        # If the node to be removed exists, update the links
        if curr.next:
            if curr.next == self.tail:  # If removing the last node, update tail
                self.tail = curr
            curr.next = curr.next.next  # Skip the target node

    def printList(self):
        """
        Print all the elements in the linked list.
        """
        curr = self.head.next  # Start from the first real node (skip dummy head)
        while curr:
            print(curr.val, "->", end=" ")
            curr = curr.next
        print("None")  # End of the list
