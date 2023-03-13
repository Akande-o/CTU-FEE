import math
def circle_chars(radius):
    """Return a circumference and an area of a circle.
 
    :param radius: int radius of a circle.
    :return: (int, int) tuple containing circumference and area (in this order)
    >>> circle_chars(3)
    (18.84955592153876, 28.274333882308138)
    """
    c = 2 * math.pi * radius
    a = math.pi * (radius**2)
    return (c, a)

if __name__ == "__main__":
    import doctest
    doctest.testmod()