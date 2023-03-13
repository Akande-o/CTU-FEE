def sum_decimals_in_string(s):
    """Return sum of decimal numbers in a string.
    :param s: string containing the decimal numbers separated by ','
    :return: float, sum of all decimals
 
    Examples:
    >>> sum_decimals_in_string('1.2')
    1.2
    >>> sum_decimals_in_string('1.2,3.4')
    4.6
    >>> sum_decimals_in_string('1,2,0.000001')
    3.000001
    """
    sum = 0
    #, is delimiter here
    num_list = s.split(",")
    for str_num in num_list:
        sum += float(str_num)
    return sum

if __name__ == "__main__":
    import doctest
    doctest.testmod() 