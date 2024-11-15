# Class representing a single node in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Value of the node
        self.ref = None   # Reference to the next node (default is None)

# Class representing a singly linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the linked list with no nodes (empty list)

    # Method to print the linked list
    def print_LL(self):
        if self.head is None:  # Check if the list is empty
            print("Linked list is empty!")
        else:
            n = self.head  # Start from the head
            while n is not None:  # Traverse until the end of the list
                print(n.data, end=" -> ")
                n = n.ref
            print("None")  # End of the list

    # Method to add a node at the beginning of the linked list
    def add_begin(self, data):
        new_node = Node(data)  # Create a new node
        new_node.ref = self.head  # Link the new node to the current head
        self.head = new_node  # Update the head to the new node

    # Method to add a node at the end of the linked list
    def add_end(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty, set the new node as the head
            self.head = new_node
        else:
            n = self.head  # Start from the head
            while n.ref is not None:  # Traverse to the last node
                n = n.ref
            n.ref = new_node  # Link the last node to the new node

    # Method to add a node after a specific value
    def add_after(self, data, x):
        n = self.head  # Start from the head
        while n is not None:
            if x == n.data:  # Find the node with value `x`
                break
            n = n.ref
        if n is None:  # If the node with value `x` is not found
            print("Node is not present in the linked list")
        else:
            new_node = Node(data)  # Create a new node
            new_node.ref = n.ref  # Link the new node to the next node
            n.ref = new_node  # Link the current node to the new node

    # Method to add a node before a specific value
    def add_before(self, data, x):
        if self.head is None:  # If the list is empty
            print("Linked List is empty!")
            return
        if self.head.data == x:  # If the node to add before is the head
            self.add_begin(data)
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:  # Find the node before the node with value `x`
                break
            n = n.ref
        if n.ref is None:  # If the node with value `x` is not found
            print("Node is not found!")
        else:
            new_node = Node(data)  # Create a new node
            new_node.ref = n.ref  # Link the new node to the target node
            n.ref = new_node  # Link the previous node to the new node

    # Method to insert a node in an empty linked list
    def insert_empty(self, data):
        if self.head is None:  # Check if the list is empty
            new_node = Node(data)  # Create a new node
            self.head = new_node  # Set the new node as the head
        else:
            print("Linked List is not empty!")

    # Method to delete the first node in the linked list
    def delete_begin(self):
        if self.head is None:  # If the list is empty
            print("Linked List is empty, can't delete!")
        else:
            self.head = self.head.ref  # Update the head to the next node

    # Method to delete the last node in the linked list
    def delete_end(self):
        if self.head is None:  # If the list is empty
            print("Linked List is empty, can't delete nodes!")
        elif self.head.ref is None:  # If there is only one node
            self.head = None  # Set the list to empty
        else:
            n = self.head
            while n.ref.ref is not None:  # Traverse to the second last node
                n = n.ref
            n.ref = None  # Remove the reference to the last node

    # Method to delete a node by value
    def delete_by_value(self, x):
        if self.head is None:  # If the list is empty
            print("Can't delete, Linked List is empty!")
            return
        if x == self.head.data:  # If the node to delete is the head
            self.head = self.head.ref  # Update the head
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:  # Find the node with value `x`
                break
            n = n.ref
        if n.ref is None:  # If the node with value `x` is not found
            print("Node is not present!")
        else:
            n.ref = n.ref.ref  # Remove the node by updating the links


