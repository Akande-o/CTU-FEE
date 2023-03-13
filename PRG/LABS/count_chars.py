def count_chars(string, char):
    """Return the number of occurances of char in string.
 
    :param string: a string. Example "hello world"
    :param char: character. Example "l"
    :return: int number of char occurences in string
    >>> count_chars("hello","l")
    2
    >>> count_chars("hippopotamus", "p")
    3
    """
    counter = 0
    for letter in string:
        if letter == char:
            counter += 1
    return counter

if __name__ == "__main__":
    import doctest
    doctest.testmod()
