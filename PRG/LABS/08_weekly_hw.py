def read_elements(filename):
    """Return a list of lists with info about chem. elements read from the given file
 
    :param filename: string, path to a file with the elements database
    :return: list of tuples, each tuple containing name (string), number (int),
             and weight (float) for each element.
    """ 
    myfile = open(filename, "r", encoding = 'utf-8')
    elements = []

    for line in myfile:
        a, b, c = line.split()
        b = int(b)
        c = float(c)
        elements.append((a,b,c))
    return elements
        

if __name__ == "__main__":
    print(read_elements('elements.txt'))