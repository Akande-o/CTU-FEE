def reverse_string(string):
    """Return a reversed version of string.
 
    :param string: string to be reversed
    :return: reversed string
    >>> reverse_string("hello")
    'olleh'
    """
    new_string = ""
    for letter in string:
        new_string = letter + new_string
    return new_string
