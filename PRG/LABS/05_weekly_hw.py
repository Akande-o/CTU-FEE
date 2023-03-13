def combine_elements(el1, el2):
    """Return a list of possible compounds each containing a single element from both the first and second list.
    :param el1: list of strings, symbols of chemical elements for the first place of compound
    :param el2: list of strings, symbols of chemical elements for the second place of compound
    :return: list of strings, possible chemical compounds
 
    Example:
    >>> metals = 'Li Na K'.split()
    >>> halogens = 'F Cl Br'.split()
    >>> print(combine_elements(metals, halogens))
    ['LiF', 'LiCl', 'LiBr', 'NaF', 'NaCl', 'NaBr', 'KF', 'KCl', 'KBr']
    """
    chem_compounds = []
    for first_el in el1:
        for second_el in el2:
            compounds = first_el + second_el
            chem_compounds.append(compounds)
    return chem_compounds

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    