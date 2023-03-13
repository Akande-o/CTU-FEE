import itertools
def solve(equation):
    """Find all solutions to the given character equation
 
    :param equation: string, the specification of the character equation
    :return: list of strings, solutions to the equation, 
                 all characters are replaced by numbers and the equation holds; 
             empty list, if no solution is found.
    >>> solve('A + AB + ACC == BCCC')
    ['9 + 91 + 900 == 1000']
    >>> solve('(J + O + I + N + T)**3 == JOINT')
    ['(1 + 9 + 6 + 8 + 3)**3 == 19683']
    >>> solve('ABC + ADC == DECA')  # Two solutions!!!
    ['834 + 814 == 1648', '879 + 819 == 1698']
    """
    #initialize the lists to be used to solve the puzzle
    solutions = []   # the list of the answers to the puzzles
    char_equation = []  # the list of each unique characters in the puzzle 
    not_zero_chars = [] # the list of first digits in numbers which can't be zero

    equation_1 = equation  # creating a copy of the original equation for easier computation

    #iterate through the equation and remove any numeric or mathematical operation character
    for symbol in equation_1:       
        if not symbol.isalpha():
            equation_1 = equation_1.replace(symbol, ' ')
    # using the split function to get the each number as a whole by removing the excess whitespaces created above
    numbers = equation_1.split()
    #iterate through the numbers in the equation and get the first digit and add it to the not_zero_chars list
    # add the first digit of each number to the characters of the equation firt for easier computation later
    for num in numbers:    
        if len(num) > 1 and num[0] not in not_zero_chars: 
            not_zero_chars.append(num[0])
            char_equation.append(num[0]) 
    # to get the other characters in the equation we need to iterate through each letter in the equation
    # and make sure they are added to the character equation list  
    for letters in numbers:
        for char in letters:
            if char not in char_equation:
                char_equation.append(char)
    
    # since we appended the non-zero elements first we would need to compute the length of the list for computation
    num_zero = len(not_zero_chars)
    values = '0123456789'       # the possibilities of the each digit in the numbers
    zero = values[0]            # the zero element for the first digit of each number
    
    # create the permutations for all possibilities of numbers in the equation
    for perm in itertools.permutations(values, len(char_equation)):
        #since we appended non-zero elements first, using indexing and the length of the list we can ensure 
        # the non-zero elements are never zero by making sure the first num_zero elements are not zero 
        if zero not in perm[:num_zero]:         
            chars_to_replace = "".join(char_equation) # converting the list of characters in the equation to a string
            digits = "".join(perm)  # converting each permutation to a string
        #using the maketrans() method to get the mapping from characters in the equation to the digits of the permutation  
            tab = str.maketrans(chars_to_replace, digits) 
            #using the translate() to create the copy of the permutation in the string
            equation_num = equation.translate(tab)
            #using the eval() function to do the computation and confirm if it is true or false
            if eval(equation_num): 
                solutions.append(equation_num)  # return thee permutation if it is true

    return solutions     
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(solve('(J + O + I + N + T)**3 == JOINT'))
    print(solve('A + AB + ACC == BCCC'))
    print(solve('ABC + ADC == DECA'))
    print(solve('GO + MOO + GO == LAME'))
    print(solve('ABC + CBA == DDD'))
    print(solve('VIOLIN * 2 + VIOLA == TRIO + SONATA'))
    print(solve('NORTH / SOUTH == EAST / WEST'))