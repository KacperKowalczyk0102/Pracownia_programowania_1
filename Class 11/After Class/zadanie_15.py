# Zadanie 15

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'P({self.x},{self.y})'

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return "The distance beetwen points is 0"
        else:
            x = (self.x - other.x)
            y = abs(self.y - other.y)
            return (x**2 + y**2)**1/2

p1 = Point(1,2)
p2 = Point(1,2)
p3 = Point(3,4)
p4 = Point(4,5)

print(p1)
print(p2)
print(p3)
print(p4)
print(p1 == p2)
print(p3 == p4)
