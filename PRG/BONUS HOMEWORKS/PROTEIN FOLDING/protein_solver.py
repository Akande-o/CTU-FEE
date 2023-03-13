import matplotlib.pyplot as plt
from folding import positions, fold, score
def solve(amino):
    """The function returns a sequence (list, string or tuple) of the optimally folded configuration of an amino acid sequence
    Parameters:
    amino - The sequence of the amino acid sequence 
    Returns:
    opt - The sequence of a optimally folded configuration of length (len(amino) - 1)"""
    # Initially make sure the input amino acid sequence is a string of 0s and 1s
    try:
        type(amino) == str or type(amino) == list 
    except:
        raise TypeError ("the amino acid sequence must be a sequence of numbers")
    # Initialise some of the sequences we would be using to compute the final configuration
    c1 = []
    c2 = []
    c = []
    if type(amino) == str:         # the case when amino is a string sequence
        # Initialising the list of the sequence of the amino acid
        a_list = []
    
        # Converting the string to a list of numbers for easier computation
        for num in amino:
            num = int(num)
            a_list.append(num)
    else:
        a_list = list(amino)

    # Further initialisation of the sequence of the list of configurations
    for i in range(len(amino)-1):
        c.append(1)
        c1.append(1)
        c2.append(1)
    prev_zero = []    # The list consisting of the index for which zeros in the sequence are preceded by a 1
    next_zero = []    # The list consisting of the index for which zeros in the sequence are followed by a 1
    n = 0

    # Iterating through the sequence to get the hydrophobic components 
    for i in a_list:
        n += 1    # computing the index of the specific hydrophobic components we are trying to add to the list
        
        # getting the specific hydrophobic components which are preceded by a 1
        if i == 0 and n == 1 or i == 0 and a_list[n - 2] == 1:
            prev_zero.append(n)
        # getting the specific hydrophobic components which are followed by a 1
        if i == 0 and n == len(amino) or i == 0 and a_list[n] == 1:
            next_zero.append(n)
    # Now we have the specific hydrophobic components we are looking for. So, we would try to bend the sequence in a way 
    # that we get the hydrophobic components clustered together as much as possible

    # Considering the condition when the first set of hydrophobic components which is preceded and followed by 1
    # and find out if they are different from each other 
    t = len(prev_zero) - 1
    if prev_zero[0] < next_zero[0]: # when they are different
        
        # when we want to get the configuration we would consider the sets of hydrophobic components using iteration
            for i in range(len(prev_zero)):
            # we would consider it for all concerning except for the last set of hydrophobic components
                if i < t:
                    if a_list[0] == 1:               # The case when the sequence starts with a set of hydrophilic components
                    # iterating through the the first set of hydrophilic proteins to make sure they are more compacted
                        for b in range(prev_zero[0] - 1):
                            c1[b] = 1j
                            c2[b] = 1j
                    if prev_zero[i] == next_zero[i]: # when any of the other set of zeros except for the first or last and there is just one 0
                        c1[prev_zero[i] - 1] = 1j    # putting the 0 compacted together to make sure we get an optimal fold 
                    
                    else:                          # when considering set of zeros in the amino acid and there are more than one 0s  
                        for num in range(prev_zero[i] - 1, next_zero[i] - 1):  # putting all 0s compacted together to make sure we get an optimal fold
                                c1[num] = 1j
                        # computing the bending point for the hydrophilic components which must also be close to get an optimal fold
                        mid_zero = (prev_zero[i+1] + next_zero[i] - 1) / 2  
                        if mid_zero != int(mid_zero):  # when it doesn't have an integer bend point
                            mid_zero = int(mid_zero) + 1 # we round up to the nearest integer
                            c1[next_zero[i] - 1] = 1j     # we move the first 1 in the sequence up to make sure it is still an optimal fold
                        # to make sure the configuration is compacted, we would bend the sequence perpendicularly
                        for index in range(int(mid_zero - 1), prev_zero[i+1] - 1):
                            c1[index] = 1j
                            # we structure the configuration to fold perpendicularly once more, to make it more compacted
                            if index == mid_zero - 1:  # we skip the mid bend point to make sure its self-avoiding
                                continue
                            else:
                                c2[index] = 1j
            
            # Considering the last set of zeros in the sequence
            else:
                for num in range(prev_zero[t] - 1, next_zero[t]- 1):   # Compacting the last set of hydrophobic components
                    c1[num] = 1j
    
    # Considering the case that the first set of zeros is just one i.e preceded and followed by 1s (there is only one zero)
    else:
        
        # Considering the case when the first set of hydrophobic proteins is just one 0 and it is the first 
        if prev_zero[0] == 1:    # considering the case when it is the first protein in the sequence
            c1[0] = 1j
        else:                    # considering the case when it is not the first protein in the sequence
            c1[prev_zero[0] - 2] = 1j
            c1[prev_zero[0] - 1] = 1
        
        # computing the bending point for the hydrophilic components which must also be close to get an optimal fold
        mid_zero = (prev_zero[1] + prev_zero[0] - 1) / 2
        if mid_zero != int(mid_zero):        # when it doesn't have an integer bend point
            mid_zero = int(mid_zero) + 1      # we round up to the nearest integer
        
        # to make sure the configuration is compacted, we would bend the sequence perpendicularly
        for index in range(int(mid_zero - 1), prev_zero[1] - 1):
                    c1[index] = 1j
                    # we structure the configuration to fold perpendicularly once more, to make it more compacted
                    if index == mid_zero - 1:  # we skip the mid bend point to make sure its self-avoiding
                        continue
                    else:             
                        c2[index] = 1j       
        
        # We are looking at the case for the other set of hydrophobic components except for the last set of proteins
        for i in range(1, len(prev_zero)):
            if i < t:
                if prev_zero[i] == next_zero[i]:    # when any of the other set of zeros except for the first or last and there is just one 0
                    c1[prev_zero[i] - 1] = 1j       # putting the 0 compacted together to make sure we get an optimal fold
                else:
                    for num in range(prev_zero[i] - 1, next_zero[i] - 1):   # when considering set of zeros in the amino acid and there are more than one 0s
                        c1[num] = 1j     # putting all 0s compacted together to make sure we get an optimal fold
                
                # computing the bending point for the hydrophilic components which must also be close to get an optimal fold
                mid_zero = (prev_zero[i+1] + next_zero[i] - 1) / 2
                if mid_zero != int(mid_zero):    # when it doesn't have an integer bend point
                    mid_zero = int(mid_zero) + 1  # we round up to the nearest integer
                    c1[next_zero[i] - 1] = 1j     # we move the first 1 in the sequence up to make sure it is still an optimal fold
                
                # to make sure the configuration is compacted, we would bend the sequence perpendicularly
                for index in range(int(mid_zero - 1), prev_zero[i+1] - 1):
                    c1[index] = 1j
                    # we structure the configuration to fold perpendicularly once more, to make it more compacted
                    if index == mid_zero - 1:   # we skip the mid bend point to make sure its self-avoiding
                        continue
                    else:
                        c2[index] = 1j
            else:
                for num in range(prev_zero[t] - 1, next_zero[t]- 1):
                    c1[num] = 1j
    
    # We are trying to fold it perpendicularly at first to get it more compact
    c3 = fold(c, c1)
    
    # Next, we fold it one more time and we get the optimal fold configuration which is very compact
    opt = fold(c3, c2)
    return opt

def visualise(amino, opt):
    """
    The function takes in the amino acid sequence and the optimal folding configuration and 
    displays the configuration graphically.
    Parameters:
    amino - The sequence of the amino acid sequence
    opt- The sequence of a optimally folded configuration of length (len(amino) - 1) """
    # computing the x and y co-ordinates of the configuration of the amino acid at each vertex
    p = positions(opt)

    # Initialising the co-ordinates of the configuration of the optimal folded configuration
    x = []
    y = []

    # Using the idea of complex numbers to get each vertex and seperating the co-ordinates
    for num in p:
        r = num.real        #the real component in each complex number
        q = num.imag        #the imaginaring component in each complex number
        
        #appending the real and imaginary component to the respective axes (list)
        x.append(r)
        y.append(q)
    # iterating through each element in the amino acid 
    for i in range(len(p)):
        # using the blue colour and round vertex for hydrophobic components
        if amino[i] == "0" or amino[i] == 0:
            plt.plot(p[i].real, p[i].imag, "bo")
        # using the red colour and round vertex for hydrophobic components
        else:
            plt.plot(p[i].real, p[i].imag, "ro")
    # using a black line to show the folding of the sequence
    plt.plot(x,y,"k")
    plt.show()       # to display the graph

c = solve("11111100000000000000000111111111111111000011100000000000000000011")
visualise("11111100000000000000000111111111111111000011100000000000000000011", c)
        


            