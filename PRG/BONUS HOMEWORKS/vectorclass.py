class Vector:
    def __init__(self,x):
        """
        constructor of the Vector class
        input:
        x - list or tuple of lenght
        sets:
        self.x - tuple: the vector values
        self.n - vector length
        >>> v = Vector([1,2,3])
        """
        self.x = tuple(x)
        self.n = len(x)
 
    def scaled_copy(self, scale):
        """ 
        Isotropic scaling, scalar multiplication, in fact
        https://en.wikipedia.org/wiki/Scaling_(geometry)
 
        >>> v = Vector([1,2,3])
        >>> v2 = v.scaled_copy(3)
        >>> v.x
        (1, 2, 3)
        >>> v2.x
        (3, 6, 9)
        """
        scaled = []
        for value in self.x:
            sc_value = scale * value
            scaled.append(sc_value)
        return Vector(scaled)

 
    def __add__(self,other):
        """
        overloading the + operator
 
        :return: Vector object result of the addition, None if not possible (not compatible vectors)
        """
        added = []
        if len(self.x) == len(other.x):
            for i in range(len(self.x)):
                add_vec = self.x[i] + other.x[i]
                added.append(add_vec)
            return Vector(added)
        return None
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)