import mymath
cos_values = []
sin_values = []
def get_trig_series(lst):
    """Return lists of cosines and sines of the values in the input list 
        :param lst: list of floats, input values for this cos and sin functions are to be computed
        :return: list of floats, approximate cosines
        :return: list of floats, approximate sines
 
        Example:
        >>> cs, sn = get_trig_series([0, 0.1])
        >>> print(cs, sn)
        [1.0, 0.9900041666666667] [0.0, 0.09983341666666667]
        """
    for input in lst:
        cosine_input = mymath.cos(input)
        sine_input = mymath.sin(input)
        cos_values.append(cosine_input)
        sin_values.append(sine_input)
    return cos_values, sin_values

if __name__ == "__main__":
    import doctest
    doctest.testmod()

        
