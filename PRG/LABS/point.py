import copy
class Point:
    """Representation of a 2D point."""
 
    def __init__(self, x, y):
        """Initializes the Point object.
 
    Attributes:
        x (float): x coordinate of the point.
        y (float): y coordinate of the point.
    """
        self.x = x
        self.y = y
 
    def move(self, dx, dy):
        return Point(self.x + dx, self.y + dy)
 
    def __str__(self):
        return "Point(x={}, y={})".format(self.x, self.y)
 
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

def move_point(p, dx, dy):
    p.x += dx
    p.y += dy
class Rectangle:
    """Representation of a rectangle"""
 
    def __init__(self, corner, height, width):
        """Initializes the Rectangle object.
 
        Attributes:
        corner (Point): coordinates of the left upper corner of the rectangle.
        height (float): height of the rectangle.
        width (float): width of the rectangle.
        """
        self.corner = corner
        self.height = height
        self.width = width
 
    def __str__(self):
        return "Rectangle({}, h={}, w={})".format(str(self.corner), self.height, self.width)
 
    def __eq__(self, other):
        return (self.corner == other.corner and 
        self.height == other.height and 
        self.width == other.width)
if __name__ == "__main__":
    p1 = Point(2, 3)
    print(p1)
 
    # dot operator composition
    p2 = p1.move(1, -2)
    print(p2)
    p3 = p1.move(1, 0).move(0, -2)
    print(p3)
    # objects mutable
    print(p1)
    move_point(p1, 2, 3)
    print(p1)
    r1 = Rectangle(Point(2, 3), 10, 8)
    print("r1:", r1)
 
    # copy using the "=" operator
    # only reference is copied
    # difference variables pointing to the exact same object
    r2 = r1
 
    print("r1 == r2: ", r1 == r2)
    print("r1 is r2: ", r1 is r2)
 
    print("\nr2.height = 5")
    r2.height = 5
    print("r1:", r1)
    print("r2:", r2)
    print("r1 == r2: ", r1 == r2)
    print("r1 is r2: ", r1 is r2)
 
    print("\nr2.corner.x = 0")
    r2.corner.x = 0
    print("r1:", r1)
    print("r2:", r2)
    print("r1 == r2: ", r1 == r2)
    print("r1 is r2: ", r1 is r2)

    # copy using the copy.copy() function
    # copy only 1 level deep
    # called a shallow copy
    r3 = copy.copy(r1)
 
    print("r1 == r3: ", r1 == r3)
    print("r1 is r3: ", r1 is r3)
 
    print("\nr3.height = 5")
    r3.height = 5
    print("r1:", r1)
    print("r3:", r3)
    print("r1 == r3: ", r1 == r3)
    print("r1 is r3: ", r1 is r3)
 
    print("\nr3.corner.x = 0")
    r3.corner.x = 0
    print("r1:", r1)
    print("r3:", r3)
    print("r1 == r3: ", r1 == r3)
    print("r1 is r3: ", r1 is r3)

     # copy using the copy.deepcopy() function
    # copy of the child objects (recursively)
    # called a deep copy
    r4 = copy.deepcopy(r1)
 
    print("r1 == r4: ", r1 == r4)
    print("r1 is r4: ", r1 is r4)
 
    print("\nr4.height = 5")
    r4.height = 5
    print("r1:", r1)
    print("r4:", r4)
    print("r1 == r4: ", r1 == r4)
    print("r1 is r4: ", r1 is r4)
 
    print("\nr4.corner.x = 0")
    r4.corner.x = 0
    print("r1:", r1)
    print("r4:", r4)
    print("r1 == r4: ", r1 == r4)
    print("r1 is r4: ", r1 is r4)