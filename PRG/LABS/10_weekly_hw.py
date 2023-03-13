class Book:
    """represents a book"""
 
    def __init__(self, title, author, year):
        """
        :param title: string, book title
        :param author: string, book author
        :param year: int, year of publication
        """
        self.title = title
        self.author = author
        self.year = year
 
    def __str__(self):
        """
        >>> book1 = Book("I, Robot", "Isaac Asimov", 1950)
        >>> print(book1)
        Book: I, Robot by Isaac Asimov (1950)
        >>> book2 = Book("Pride and Prejudice", "Jane Austen", 1813)
        >>> print(book2)
        Book: Pride and Prejudice by Jane Austen (1813)
        """
        return "Book: {} by {} ({})".format(self.title, self.author, self.year)
 
    def has_same_author(self, other):
        """Compares authors of this and the other book.
 
        :param other: Book object
        :return: boolean, True if self and other have the same author, otherwise False
        >>> book1 = Book("I, Robot", "Isaac Asimov", 1950)
        >>> book2 = Book("Pride and Prejudice", "Jane Austen", 1813)
        >>> book3 = Book("Sense and Sensibility", "Jane Austen", 1811)
        >>> book1.has_same_author(book3)
        False
        >>> book2.has_same_author(book3)
        True
        """
        return self.author == other.author
 
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)