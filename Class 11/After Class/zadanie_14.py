# Zadanie 14

import math

class Area:

    @staticmethod
    def circle(r):
        p = math.pi * r**2
        return p

    @staticmethod
    def rectangle(a, b):
        p = a * b
        return p

    @staticmethod
    def triangle(a, h):
        p = (a * h)/2
        return p


p1 = Area.circle(3)
p2 = Area.rectangle(4, 7)
p3 = Area.triangle(6, 2)
print(p1)
print(p2)
print(p3)