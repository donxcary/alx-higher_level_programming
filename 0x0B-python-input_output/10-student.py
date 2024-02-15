class Student:
    """
    This class defines a student by first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        This method initializes a Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This method retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, only attribute names contained in this list are retrieved.
        Otherwise, all attributes are retrieved.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if attr in self.__dict__}
