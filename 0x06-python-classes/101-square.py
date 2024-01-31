#!/usr/bin/python3
"""
Module 101-square
Defines class Square
"""

class Square:
    """A class that defines a square by its size and position"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with an optional size and position"""

        # Set the size and position attributes using the properties
        self.size = size
        self.position = position

    @property
    def size(self):
        """Return the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""

        # Check if value is an integer
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        # Check if value is positive or zero
        if value < 0:
            raise ValueError("size must be >= 0")

        # Set the size attribute
        self.__size = value

    @property
    def position(self):
        """Return the position of the square"""

        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square"""

        # Check if value is a tuple of two positive integers
        if not (isinstance(value, tuple) and len(value) == 2 and
                isinstance(value[0], int) and value[0] >= 0 and
                isinstance(value[1], int) and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        # Set the position attribute
        self.__position = value

    def area(self):
        """Return the current square area"""

        # Calculate the area as size squared
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character #"""

        # Check if size is zero
        if self.__size == 0:
            # Print an empty line
            print()

        else:
            # Print the position offset in the first line
            print("\n" * self.__position[1], end="")

            # Loop through the rows of the square
            for i in range(self.__size):
                # Print the position offset in each row
                print("_" * self.__position[0], end="")

                # Print the character # in each column
                print("#" * self.__size)

                # Print a newline character after each row
                print()

    def __str__(self):
        """Return a string representation of the square"""

        # Initialize an empty string to store the output
        output = ""

        # Check if size is zero
        if self.__size == 0:
            # Append an empty line to the output
            output += "\n"

        else:
            # Append the position offset in the first line to the output
            output += "\n" * self.__position[1]

            # Loop through the rows of the square
            for i in range(self.__size):
                # Append the position offset in each row to the output
                output += "_" * self.__position[0]

                # Append the character # in each column to the output
                output += "#" * self.__size

                # Append a newline character to the output
                output += "\n"

        # Return the output without the last newline character
        return output[:-1]