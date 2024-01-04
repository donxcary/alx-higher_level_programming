#!/usr/bin/python3
"""
Module 100-singly_linked_list
Defines class Node and class SinglyLinkedList
"""


class Node:
    """
    A class that defines a node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node
        if type(data) is not int:
            raise TypeError("data must be an integer")
        if type(next_node) is not Node:
            if next_node is not None:
                raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        self.__next_node = value


class SinglyLinkedList:
    """
    A class that defines a singly linked list
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
            tmp = self.__head
        else:
            tmp = self.__head
            small = self.__head
            while tmp is not None:
                if tmp.data <= small.data:
                    small = tmp
                tmp = tmp.next_node
            self.__head = small
            tmp = self.__head
            new_node = Node(value)
            while tmp is not None:
                if tmp.data == new_node.data:
                    break
                if new_node.data <= small.data:
                    node1 = small
                    small = new_node
                    new_node = node1
                    self.__head = small
                    tmp = self.__head
                    tmp.next_node = new_node
                elif new_node.data <= tmp.data:
                    node1 = tmp
                    tmp = new_node
                    new_node = node1
                    tmp.next_node = new_node
                    node2 = tmp
                    tmp = self.__head
                    while tmp.next_node.data != node2.next_node.data:
                        tmp = tmp.next_node
                    tmp.next_node = node2
                else:
                    if tmp.next_node != new_node:
                        if tmp.next_node is None:
                            tmp.next_node = new_node
                tmp = tmp.next_node

    def __repr__(self):
        while self.__head.next_node is not None:
            print(self.__head.data)
            self.__head = self.__head.next_node
        return "%s" % (self.__head.data)
