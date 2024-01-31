#!/usr/bin/python3
"""
Module 100-singly_linked_list
Defines class Node and class SinglyLinkedList
"""

class Node:
    """A class that defines a node of a singly linked list by its data and next node"""

    def __init__(self, data, next_node=None):
        """Initialize the node with data and next node"""

        # Set the data and next node attributes using the properties
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Return the data of the node"""

        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node"""

        # Check if value is an integer
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        # Set the data attribute
        self.__data = value

    @property
    def next_node(self):
        """Return the next node of the node"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node of the node"""

        # Check if value is None or a Node
        if not (value is None or isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")

        # Set the next node attribute
        self.__next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list by its head"""

    def __init__(self):
        """Initialize the list with an empty head"""

        # Set the head attribute to None
        self.__head = None

    def __str__(self):
        """Return a string representation of the list"""

        # Initialize an empty list to store the node data
        node_data = []

        # Initialize a variable to point to the head node
        current = self.__head

        # Loop through the nodes until the end of the list
        while current is not None:
            # Append the node data to the list
            node_data.append(str(current.data))

            # Move to the next node
            current = current.next_node

        # Return the list as a string with newline characters
        return "\n".join(node_data)

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list"""

        # Create a new Node with the given value
        new_node = Node(value)

        # Check if the list is empty or the value is smaller than the head node data
        if self.__head is None or value < self.__head.data:
            # Insert the new node at the beginning of the list
            new_node.next_node = self.__head
            self.__head = new_node

        else:
            # Initialize a variable to point to the head node
            current = self.__head

            # Loop through the nodes until the end of the list or the value is smaller than the next node data
            while current.next_node is not None and value >= current.next_node.data:
                # Move to the next node
                current = current.next_node

            # Insert the new node after the current node
            new_node.next_node = current.next_node
            current.next_node = new_node
