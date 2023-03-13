def sum_digits_in_string(s):
    """Return sum of all digits in a string.
    :param s: string containing the digits and other characters
    :return: numeric value, sum of all digits
 
    Examples:
    >>> sum_digits_in_string('1')
    1
    >>> sum_digits_in_string('hi 1 hello 2')
    3
    >>> sum_digits_in_string('Values: 1.26, 2.3, 1.76')
    28
    """
    sum = 0
    for character in s:
        if character.isnumeric():
            sum += int(character)
    return sum

if __name__ == "__main__":
    import doctest
    doctest.testmod()