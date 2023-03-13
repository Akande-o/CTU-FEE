def replace_chars(string, char_original, char_replacement):
    """Return a new string with all occurences of char_original replaced by char_replacement.
 
    :param string: string in which some chars shall be replaced
    :param char_original: character to be replaced
    :param char_replacement: character to be inserted instead of char_original
    :return: a new string with replaced characters
    >>> replace_chars("hello","h","H")
    'Hello'
    >>> replace_chars("hello","l","L")
    'heLLo'
    """
    new_str = ""
    for letter in string:
        if letter == char_original:
            new_str += char_replacement
        else:
            new_str += letter
    return new_str
