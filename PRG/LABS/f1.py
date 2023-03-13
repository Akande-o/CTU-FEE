def get_square(s):
    '''Returns area and perimeter of a square

    Parameters:
        s(float) = side of the square
    Returns:
        A(float): area of a square
        P(float): perimeter of a square
    >>> get_square(1)
    (1, 4)
    >>> get_square(5)
    (25, 20)
    '''
    A = s * s
    P = 4 * s
    return A, P
if __name__ == "__main__":
    area, perimeter = get_square(10)
    print("area = ", area, "perimeter = ", perimeter)
if __name__ == "__main__":
    help(get_square)
if __name__ == "__main__":
    import doctest
    doctest.testmod()