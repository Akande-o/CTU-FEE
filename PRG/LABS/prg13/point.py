import math
 
class Point:
 
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)
 
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
 
    def get_norm(self):
        norm = math.sqrt(self.x ** 2 + self.y ** 2)
        return norm
 
    def is_unit(self):
        return self.get_norm() == 1
 
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y