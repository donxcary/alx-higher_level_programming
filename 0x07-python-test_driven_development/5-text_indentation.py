#!/usr/bin/python3
"""
Module
Please refer to the documentation in the README.md
"""


def text_indentation(text):
    """
    A simple function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        @text: string of text to be printed

    Raises:
        TypeError: Raises an exception
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    length = len(text)
    i = 0
    while i < length:
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print("{:s}\n".format(text[i]))
            i = i + 1
        elif text[i] == ' ':
            for j in range(i, length):
                if text[j] != ' ':
                    break
            letter = text[i - 1]
            if letter == '.' or letter == '?' or letter == ':':
                for k in range(i, j):
                    i = i + 1
            else:
                print("{:s}".format(text[i]), end="")
                i = i + 1
        else:
            print("{:s}".format(text[i]), end="")
            i = i + 1
