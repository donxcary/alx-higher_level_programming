#!/usr/bin/python3
"""
Module 101-square
Defines class Square
"""


class Square:
    """
    A class that defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        message = "position must be a tuple of 2 positive numbers"
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) != tuple:
            raise TypeError(message)
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
            raise TypeError(message)

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
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if type(value) != tuple or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive")
        if value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive")
        if value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive")
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
                    print()
                    a = a + 1
            c = 0
            for j in range(0, self.size):
                if c == 0:
                    for k in range(0, self.position[0]):
                        print("_", end="")
                        c = c + 1
                print("#", end="")
                if j == self.size - 1 and i != self.size - 1:
                    print("")

    def __repr__(self):
        Square.my_print(self)
        return ""
