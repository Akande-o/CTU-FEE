def scalar_mult(sc, v):
    """
    scalar multiplication (scalar * vector)
    :param sc: a scalar mulitplier
    :param v: a list - vector
    :return: sc * v
    Examples:
    >>> mult_list = scalar_mult(4, [1, 2, 3])
    >>> print(mult_list)
    [4, 8, 12]
    """ 
    scalar_v = []
    for value in v:              #iterating through every component in the vector
        values = value * sc      # multiplying each component in the vector by the specific scalar value
        scalar_v.append(values)  # returning the result of the scalar multiplication to a new list
    return scalar_v

 
def dot_product(u,v):
    """
    vector dot product
    :param u: a list
    :param v: a list
    :return:
    None if u and v are not compatible
    otherwise a number (float or int)
    Examples:
    >>> result = dot_product([1, 2], [1, 2, 3])
    >>> print(result)
    None
    >>> result = dot_product([1, 2, 3], [1, 2, 3])
    >>> print(result)
    14
    """
    dot = 0
    size = len(u) 
    if len(u) == len(v):  # testing for the compatibility of the two vectors since they must have the same dimension   
        for i in range(size):  
            dot += u[i] * v[i]  # multiplying the i, j and k elements respectively since i.i = j.j = k.k = 1
        return dot
    else:
        return None

 
def cross_product(u,v):
    """
    vector cross product, see
    :param u: a list of lenght 3
    :param v: a list of length 3
    :return:
    None if u and v are not compatible
    a list of lenght 3 - cross product of u and v
    Examples:
    >>> cross_prod = cross_product([1, 2], [1, 2, 3])
    >>> print(cross_prod)
    None
    >>> cross_prod = cross_product([2, 3, 4], [5, 6, 7])
    >>> print(cross_prod)
    [-3, 6, -3]
    """
    size = len(u)
    cross =[0, 0, 0]
    if len(u) == len(v) and size == 3:        # testing for the compatibility of the two vectors of 3 cordinates
        cross[0] = u[1] * v[2] - u[2] * v[1]   # computing the cross-product coefficient for the i-component
        cross[1] = u[2] * v[0] - u[0] * v[2]   # computing the cross-product coefficient for the j-component
        cross[2] = u[0] * v[1] - u[1] * v[0]   # computing the cross-product coefficient for the k-component
        return cross
    return None

 
def are_colinear(u,v):
    """
    testing colinearity of two vectors
    :param u: a list
    :param v: a list
    :return:
    True if u and v are colinear, False otherwise
    >>> print(are_colinear([1, 2, 3], [2, 4, 6]))
    True
    >>> print(are_colinear([1, 2, 3], [2, 4, 5]))
    False
    """
    if v[0] == 0 or u[0] == 0:                   # if either of the values is zero, they can't be colinear
        return False
    if v[0] > u[0]:                             # if the the co-ordinates of v is expected to be greater  
        number = v[0] / u[0]                    # the supposed scalar ratio value of the two vectors 
        new_vector = scalar_mult(number, u)     # the supposed larger vector proportional to the smaller
        return new_vector == v                  # test for colinearity
    else:                                       # if the the co-ordinates of u is expected to be greater 
        number = u[0] / v[0]                    #the supposed scalar ratio value of the two vectors
        new_vector = scalar_mult(number, v)     # the supposed larger vector proportional to the smaller
        return new_vector == u                  # test for colinearity

def are_perpendicular(u,v):
    """
    testing perpendicularity of two vectors
    :param u: a list
    :param v: a list
    :return:
    True if u and v are perpendicular, False otherwise
    Example:
    >>> print(are_perpendicular([1,2,1], [1,-1,1]))
    True
    """
    if len(u) == len(v):                    #the dimensions must be the same
        perp_vector = dot_product(u, v)     
        if perp_vector == 0:                # the dot product has to be zero since cos(90) = 0
            return True
        else:
            return False
    else:
        return False
 
if __name__ == "__main__":
    import doctest
    doctest.testmod()