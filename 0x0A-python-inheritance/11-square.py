#!/usr/bin/python3
""" module - base geometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):

    """ Square inheriting from Rectangle"""

    def __init__(self, size):
        """ Initializing instance with args: wdth and height of rectangle """

        self.integer_validator("size", size)
        super().__init__size(size, size)
        self.__size = size

    def __str__(self)
        """ Returns a formatted string """

        return str("[Square] {}/{}".format(self.__size, self.__size))
    def area(self):
        """ area of instance Square """
        return self.__size ** 2


