def cos(x):
    """Returns an approximate value of cos(x).
    :param x: float, input value for which the cosine function is computed
    :return: float, approximate value of cos(x)
    """
    cosine_x = 1 - x**2/2 + x**4/24
    return cosine_x
 
def sin(x):
    """Returns an approximate value of sin(x).
    :param x: float, input value for which the sine function is computed
    :return: float, approximate value of sin(x)
    """
    sine_x = x - x**3/6 + x**5/120
    return sine_x