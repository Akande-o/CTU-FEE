def my_pwc_function(x):
    """Returns a function value of the piecewise function specified in the problem setting
 
    :param x: float, parameter of the mathematical function
    :return: float, corresponding function value 
    :raises: ValueError: for such 'x' where the piecewise function is undefined
 
    >>> my_pwc_function(5)
    5.0
    >>> my_pwc_function(3)
    2.5
    """
    if x >= 6:
        f = (x-6)**2 + 5
    elif x >=4 and x < 6:
        f = 5
    elif x >= 2 and x < 4:
        f = 5*x/2 - 5
    else:
        raise ValueError 
    return float(f)

def get_function_values(par_lst):
    """Returns dictionary where the key are numbers from par_list and values are corresponding
    function values.
 
    :param par_lst: list of floats, values to be passed to the piecewise function
    :return: dict of x:my_pwc_function(x), function values
 
    >>> get_fuction_values([5, 1, 3])
    {5: 5.0, 1: 'NA', 3: 2.5}
 
    """
    func_dict = {}
    for value in par_lst:
        try:
            func = my_pwc_function(value)
            func_dict[value] = func
        except ValueError:
            func_dict[value] = 'NA'
    return func_dict 




if __name__ == "__main__":
    import doctest
    doctest.testmod()