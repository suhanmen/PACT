from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    if not numbers:
        return 0, 1
    # Initialize sum and product to the first element of the list
    s, p = numbers[0], numbers[0]
    # Loop over the rest of the list and update sum and product
    for n in numbers[1:]:
        s += n
        p *= n
    return s, p
