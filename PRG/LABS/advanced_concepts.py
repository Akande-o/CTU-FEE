"""
Examples of advanced concepts for the lecture 13
"""

import random
import os.path
from pathlib import Path


def second_element_negative(item):
    """Return second element (index 1) of an item (sequence type)"""
    return -item[1]


class Reversed:
    """An iterator that mimics the iterator returned by built-in function reversed()"""

    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        return self.iterable[self.index]


def random_number(upper_bound):
    """A generator that yields random integers in <0, upper_bound)"""
    while True:
        yield random.randint(0, upper_bound)


if __name__ == "__main__":

    points = [("Tomas", 2), ("Martin", 1), ("Anna", 10)]

    #
    # Lambda functions
    #

    print("\n== Lambda functions ==")

    print(sorted(points, key=second_element_negative))
    print(sorted(points, key=lambda item: -item[1]))


    #
    # Comprehensions (list, dict and set)
    #

    print("\n== Comprehensions ==")

    # [0**2, 1**2, 2**2, .., 9**2]
    even_squares = []
    for num in range(10):
        if num**2 % 2 == 0:
            even_squares.append(num**2)
    print(even_squares)

    even_squares = [x**2 for x in range(10) if x**2 % 2 == 0]
    print(even_squares)
    double_even_squares = [2*x for x in even_squares]
    print(double_even_squares)

    # {2: "Tomas", 1: "Martin", 10: "Anna"}
    points_name = {n: x for x, n in points}
    print(points_name)

    # {"Tomas", "Martin", "Anna"}
    unique_names = {x for x, n in points}
    print(unique_names)

    # {"t", "o", "m", ..}
    unique_characters = {y.lower() for x, n in points for y in x}
    print(unique_characters)


    #
    # Built-in module pathlib
    #

    print("\n== Module pathlib ==")

    path = Path(__file__)
    print((path.parent / "foo" / "bar").parent)
    print(os.path.dirname(os.path.join(os.path.dirname(path), "foo/bar")))


    #
    # Iterables
    #

    print("\n== Iterables ==")

    iterator = Reversed(range(1_000_000_000_000))
    print(next(iterator))
    print(next(iterator))

    generator = random_number(10)
    for _, x in zip(range(10), generator):
        print(x, end=" ")
    print()

