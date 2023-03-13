def is_palindrom(string):
    """Return True if and only if the string is equal to its reversed version.
 
    :param string: string to check for palindrom
    :return: boolean
    >>> is_palindrom("aka")
    True
    >>> is_palindrom("hello")
    False
    """
    new_string = ""
    for letter in string:
        new_string = letter + new_string
    return string == new_string
