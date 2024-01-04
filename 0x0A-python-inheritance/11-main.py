#!/usr/bin/python3
Square = __import__('11-square').Square

s = Square(13)

print(s)
print(s.area())
s = Square(4)
print(s.area())
s = Square([12, 52])
print(s.area())
