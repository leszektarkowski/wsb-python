class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def info(self):
        print(self.x, self.y)

    def __get_length(self):
        return (self.x**2 + self.y**2)**0.5

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"Point in 2D, x = {self.x}, y = {self.y}"

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __set_pos(self, position):
        self.x = position[0]
        self.y = position[1]

    def __get_pos(self):
        return self.x, self.y

    length = property(fget=__get_length)
    pos = property(fset=__set_pos, fget=__get_pos)

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

p1.info()
print(p1)
l = [p1, p2]
print(l)

print(p1.x)
print(p1.y)
print(p1.length)

if p1 == p2:
    print("The same point")
else:
    print("Different points")

p1.pos = 13, 15
print(p1)
print(p1.pos)
