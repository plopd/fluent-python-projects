"""
    Source: “Fluent Python by Luciano Ramalho (O’Reilly). Copyright 2015 Luciano Ramalho, 978-1-491-94600-8.”
"""

import math
class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y

        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == "__main__":

    v1 = Vector(2, 4)
    v2 = Vector(2, 1)

    print(v1 + v2) # Vector(4,5)

    v = Vector(3, 4)
    print(abs(v)) # 5.0
    v = v * 3
    print(v) # Vector(9,12)

    print(abs(v)) # 15.0

