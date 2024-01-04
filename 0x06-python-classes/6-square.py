#!/usr/bin/python3
"""
Module 0-square
Defines class Square
"""


class Square:
    """
    A class that defines a square
    Private instance attribute: size
    Private instance attribute: position
    property def size(self): to retrieve it
    property setter def size(self, value): to set it

    Instantiation with size and error messages
    Public instance method: def area(self): that
    returns the current square area
    Public instance method: def my_print(self): that
    prints in stdout the square with the character #
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        message = "position must be a tuple of 2 positive integers"
        if type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) == 2:
            if type(position[0]) == int:
                if position[0] < 0:
                    raise TypeError(message)
            else:
                raise TypeError(message)
            if type(position[1]) == int:
                if position[1] < 0:
                    raise TypeError(message)
            else:
                raise TypeError(message)
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if value[0] < 0 or value[1] < 0 or type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        area = self.size ** 2
        return area

    def my_print(self):
        if self.size == 0:
            print()
        a = 0
        for i in range(0, self.size):
            if a == 0:
                for h in range(0, self.position[1]):
                    print("")
                    a = a + 1
            c = 0
            for j in range(0, self.size):
                if c == 0:
                    for k in range(0, self.position[0]):
                        print(" ", end="")
                        c = c + 1
                print("#", end="")
                if j == self.size - 1:
                    print()
