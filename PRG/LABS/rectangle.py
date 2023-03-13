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

class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def width(self):
        return self.p2.x - self.p1.x
    def height(self):
        return self.p2.y - self.p1.y
    def area(self):
        width = self.width()
        height = self.height()
        return width * height
    def circumference(self):
        width = self.width()
        height = self.height()
        return 2 * (width + height)
    def __str__(self):
        return "Rectangle: p1 = {}, p2 = {}".format(self.p1, self.p2)

if __name__ == "__main__":
    rect1 = Rectangle(Point(1, 2), Point(5, 5))
    print(rect1)
    print(rect1.width())
    print(rect1.height())
    print(rect1.area())
    print(rect1.circumference())

