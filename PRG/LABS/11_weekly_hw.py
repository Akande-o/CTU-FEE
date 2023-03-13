class PointPolar:
    """represents a point in polar coordinates"""
 
    def __init__(self, r, phi):
        """
        :param r: float, norm of the point
        :param phi: float, angular coordinate
        """
        self.r = r
        self.phi = phi
 
    def __str__(self):
        """
        >>> p1 = PointPolar(5.1, 0.2)
        >>> print(p1)
        Point: r=5.1, phi=0.2
        """
        return "Point: r={}, phi={}".format(self.r, self.phi)
 
    def __eq__(self, other):
        """Equality given by both parameters"""
        return self.r == other.r and self.phi == other.phi
 
    def __mul__(self, other):
        """Multiplication of 2 points"""
        new_r = self.r * other.r
        new_phi = self.phi + other.phi
        return PointPolar(new_r, new_phi)
 
    def __truediv__(self, other):
        """Division of 2 points"""
        new_r = self.r / other.r
        new_phi = self.phi - other.phi
        return PointPolar(new_r, new_phi)
 
    def __lt__(self, other):
        """Is self < other?"""
        return self.r < other.r
 
    def __le__(self, other):
        """Is self <= other?"""
        return self.r <= other.r
 
    def __gt__(self, other):
        """Is self > other?"""
        return self.r > other.r
 
    def __ge__(self, other):
        """Is self >= other?"""
        return self.r >= other.r