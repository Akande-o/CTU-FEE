def get_roots(a, b, c):
    """
    Returns a list of roots of a quadratic equation

    Parameters:
    a - The coefficient of the x**2 term in a quadratic equation
    b - The coefficient of the x term in a quadratic equation
    c - The coefficient of the constant term in a quadratic equation
    Returns:
    roots - a list of the roots to the quadratic equation
    """
    roots = []
    D = (b**2 - 4 * a * c)    #the determinant of the equation
    if D < 0:                 #the equation has no real roots since sqrt(D) doesn't exist
        roots = []
    elif D == 0:              # the determinant has one real root since D = 0
        root1 = -b / (2 * a)
        roots.append(root1)
    else:                     # the determinant has two real roots since D > 0
        root1 = (-b + D**(1/2)) / (2 * a)
        root2 = (-b - D**(1/2)) / (2 * a)
        roots.append(root1)
        roots.append(root2)
    return roots

if __name__ == "__main__":
    print(get_roots(1, -4, 4))
    print(get_roots(1, 4, 4))
    print(get_roots(1, -18, 45))
    print(get_roots(1, 1, 1))
    print(get_roots(1, 3, 1))
