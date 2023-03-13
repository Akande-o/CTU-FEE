def remove_duplicates(items):
    """Remove duplicate items.
 
    :param items: input list, can contain anything
    :return: (unique_list, duplicates)
        unique_list - a list with unique items only
        duplicates - a list with items that were in items more than once (not unique list)
     >>> remove_duplicates(['h','e','l','l','o'])
    (['h','e','l','o'],['l'])
    """
    unique_list = []
    duplicates = []
    counter = 0
    for letter in items:
        if letter not in unique_list:
            unique_list.append(letter)
            counter = 1
        else:
            counter += 1
            if counter > 1:
                duplicates.append(letter)
                
    
    return unique_list, duplicates

if __name__ == "__main__":
    print(remove_duplicates(['h','i','p','p','o', 'p', 'o','t', 'a', 'm', 'u', 's']))
    print(remove_duplicates(['h','e','l','l','o']))
    