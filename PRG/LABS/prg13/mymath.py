def abs(x):
    if isinstance(x, int) or isinstance(x, float):
        if x >= 0:
            return x
        else:
            return -x
    else:
        raise ValueError
 
def aprox_cos(x):
    if isinstance(x, int) or isinstance(x, float):
        return 1 - x ** 2 / 2 + x ** 4 / 24
    else:
        raise ValueError
 
def aprox_sin(x):
    if isinstance(x, int) or isinstance(x, float):
        return x - x ** 3 / 6 + x ** 5 / 120
    else:
        raise ValueError