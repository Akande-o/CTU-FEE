def is_right(a, b, c):
    '''Returns whether or not the three random integer numbers represent the three sides of a right-angled triangle
    Parameters:
        a, b, c - The three random integer numbers that represent three sides of a triangle
    Returns:
        True - if the three numbers represent the sides of a right-angled triangle
        False - if the three numbers do not represent the sides of a right-angled triangle  
    '''
    if type(a) != int or type(b) != int or type(c) != int:   #the values must  be integers
        print("The numbers must be integers. Please type in integers")
        return None
    elif a < 0 or b < 0 or c < 0:      #the values must not be negative integers
        print("The numbers must be positive integer numbers. Please type in positive numbers")
        return None     
    else:  # since the numbers can be given in any order we would have to consider which is the hypotenuse of the function.
           # So we consider for each values of a, b, c which it could be now that they are integers
        if a > b and a > c:       # a is the largest of the three set of values and the hypotenuse
            if a**2 == b**2 + c**2:
                return True
            else:
                return False 
        elif b > a and b > c:     # b is the largest of the three set of values and the hypotenuse
            if b**2 == a**2 + c**2:
                return True
            else:
                return False
        else:                     # c is the largest of the three set of values and the hypotenuse
            if c**2 == a**2 + b**2:
                return True
            else:
                return False

if __name__ == "__main__":
    print(is_right(10, 8, 6))
    print(is_right(8, 17, 15))
    print(is_right(5, 12, 13))
    print(is_right(10, 11, 12))
    print(is_right(10.0, 8.3, 6))
    print(is_right("10", "8", "6"))
    print(is_right(-10, -8, -6))

    



        