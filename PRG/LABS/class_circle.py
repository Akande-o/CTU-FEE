class Circle:
    """represents a circle in 2D space"""
    # constructor
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    # functions inside a class => mmethods
    def get_area(self):
        area = 3.14 * (self.r ** 2)
        return area
    
    # c1.intersects_with(c2)
    #self => c1 and other => c2
    def insersects_with(self, other):
        """Tells if this and other circles intersect or not.
 
        :param other: Circle object
        :return: boolean: True if self and other intersect, otherwise False
        """
        distance_center = ((self.x -other.x)**2 + (self.y - other.y)**2)**0.5
        return distance_center <= (self.r + other.r)

    def get_shifted_copy(self, dx, dy):
        new_circle = Circle(self.x + dx, self.y + dy, self.r)
        return new_circle

    def __str__(self):
        return "Circle: x={}, y={}, r={}".format(self.x, self.y, self.r)

        
def is_intersect(c1, c2):
    """Tells if the two circles intersect or not.
 
    :param c1: Circle object
    :param c2: Circle object
    :return: boolean: True if the c1, c2 intersect, otherwise False
    """
    #c1 and c2 intersects if d(o1, o2) <= r1 + r2
    distance_center = ((c1.x -c2.x)**2 + (c1.y - c2.y)**2)**0.5
    return distance_center <= (c1.r + c2.r)

if __name__ == "__main__":
    c1 = Circle(1, 2, 2)
    c2 = Circle(4, 6, 4)
    print(c1)
    print(c2)
    print(c1.x, c1.y, c1.r)
    print(c2.x, c2.y, c2.r)
    print(c1.get_area())
    print(is_intersect(c1,c2))
    print(c1.insersects_with(c2))
    c1_shifted = c1.get_shifted_copy(5, -4)
    print(c1.x, c1.y, c1.r)
    print(c1_shifted.x, c1_shifted.y, c1_shifted.r)
