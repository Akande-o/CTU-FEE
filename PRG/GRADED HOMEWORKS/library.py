def load_library(filepath):
    """The function reads a text file with a | seperator in each line between book authors and book names
    Parameters:
    filepath: Path to a text file (similar to the text file explained above) containing the individual books.
    Returns:
    book_dict: a dictionary where the book titles are used as keys and the authors' names are stored as values.
    >>> book_author = load_library('books.txt')
    >>> print(book_author['RUR'])
    Capek, Karel
    >>> print(book_author['Dune'])
    Herbert, Frank
    """
    book_dict = {}                                       # initialising the dictionary
    book_list = open(filepath, "r", encoding = 'utf-8')  # opening the text file to read its contents
    for line in book_list:                               # iterating the contents line by line
        line = line.strip()                              # using the strip function to remove the \n character
        title, author = line.split("|")                  # using the format of text file to split into title and author
        book_dict[title] = author                        # using the keys as book titles and values as book authors
    book_list.close()                                    # close the text file
    return book_dict                 #the dictionary using the keys as book titles and values as book authors

def index_by_author(book_dict):
    """The function reads a dictionary of book titles as keys and book authors as values and 
    returns another dictionary with the book authors as keys and their books in a list as values.
    Parameters:
    book_dict:a dictionary where the book titles are used as keys and the authors' names are stored as values.
    Returns:
    book_index: a dictionary which stores the book authors as keys and a list of their books as values
    """
    book_index = {}                            # initialising the dictionary
    for title, author in book_dict.items():    #extracting the book titles and book authors from the input dictionary
        if author not in book_index:           # adding the authors as keys in the dictionary
            book_index[author] = [title]       # setting the values as a list of first book title in input dictionary
        else:                                  # if author is in the dictionary
            book_index[author].append(title)   # add the other titles into the list of book titles by the author
    return book_index       # dictionary using the author as keys and a list of their book titles as values

def report_author_counts(lib_fpath, rep_filepath):
    """The function shall compute the number of books of each author and the total number of books, 
    and shall store this information in another text file.
    Parameters:
    lib_fpath: Path to a library text file (containing records for individual books).
    rep_filepath: Path to report text file that shall be created by this function.
    """
    report_dict = {}                                     # initialising the report dictionary
    total_num = 0                                        # initialising the total number of books
    
    # opening the text file containing the records for individual books to read its contents
    lib_file = open(lib_fpath, "r", encoding = 'utf-8')  
    
    # converting text file to dictionary of book titles as keys and book authors as values by calling load_library()
    lib_dict = load_library(lib_fpath)
    
    # converting the dictionary using keys as titles and values as books to 
    # a dictionary using the author as keys and a list of book titles by calling index_by_author()
    index_dict = index_by_author(lib_dict)
    
    # iterating through the dictionary to get the author and the corresponding list of books
    for author, books in index_dict.items():  
        num_books = len(books)               # computing the total number of books by the author
        # adding the author as keys and the number of books as values to the report dictionary
        report_dict[author] = num_books 
        total_num += num_books               # computing the total number of books in the text file
    report_dict['TOTAL BOOKS'] = total_num         # adding the total number computed above to the dictionary
    
    # open the report text file which we will write on each line the author and the corresponding number of books
    report_file = open(rep_filepath, "w", encoding = 'utf-8') 
    
    # extracting the author and the corresponding number of books by using the .items()
    for writer, num in report_dict.items():              
        report_file.write(writer +": " + str(num) + "\n")  # write the contents to the report text file
    
    lib_file.close()                  # close the text file containg the record of individual books
    report_file.close()               # close the report file containing the authors and the corresponding number of books 
    



if __name__ == "__main__":
    book_author = load_library("books.txt")
    print(book_author["RUR"])
    print(book_author['Dune'])
    book_author = {'RUR': 'Capek, Karel', 'Dune': 'Herbert, Frank', 'Children of Dune': 'Herbert, Frank'}
    books_by = index_by_author(book_author)
    print(books_by)
    print(books_by['Capek, Karel'])
    print(books_by['Herbert, Frank'])
    report_author_counts('books.txt', 'report.txt')
