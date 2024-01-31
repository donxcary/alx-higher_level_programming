#!/usr/bin/python3

class Square:
    """A class that defines a square by its size"""

    def __init__(self, size=0):
        """Initialize the square with an optional size"""

        # Set the size attribute using the property
        self.size = size

    @property
    def size(self):
        """Return the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""

        # Check if value is a number
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")

        # Check if value is positive or zero
        if value < 0:
            raise ValueError("size must be >= 0")

        # Set the size attribute
        self.__size = value

    def area(self):
        """Return the current square area"""

        # Calculate the area as size squared
        return self.__size ** 2

    def __eq__(self, other):
        """Compare two squares for equality based on their area"""

        # Check if other is a Square instance
        if isinstance(other, Square):
            # Return True if the areas are equal
            return self.area() == other.area()

        # Return NotImplemented otherwise
        return NotImplemented

    def __ne__(self, other):
        """Compare two squares for inequality based on their area"""

        # Check if other is a Square instance
        if isinstance(other, Square):
            # Return True if the areas are not equal
            return self.area() != other.area()

        # Return NotImplemented otherwise
        return NotImplemented

    def __gt__(self, other):
        """Compare two squares for greater than based on their area"""

        # Check if other is a Square instance
        if isinstance(other, Square):
            # Return True if the area of self is greater than the area of other
            return self.area() > other.area()

        # Return NotImplemented otherwise
        return NotImplemented

    def __ge__(self, other):
        """Compare two squares for greater than or equal to based on their area"""

        # Check if other is a Square instance
        if isinstance(other, Square):
            # Return True if the area of self is greater than or equal to the area of other
            return self.area() >= other.area()

        # Return NotImplemented otherwise
        return NotImplemented

    def __lt__(self, other):
        """Compare two squares for less than based on their area"""

        # Check if other is a Square instance
        if isinstance(other, Square):
            # Return True if the area of self is less than the area of other
            return self.area() < other.area()

        # Return NotImplemented otherwise
        return NotImplemented

    def __le__(self, other):
        """Compare two squares for less than or equal to based on their area"""

        # Check if other is a Square instance
        if isinstance(other, Square):
            # Return True if the area of self is less than or equal to the area of other
            return self.area() <= other.area()

        # Return NotImplemented otherwise
        return NotImplemented

