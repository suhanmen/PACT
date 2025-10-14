from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    
    # initialization of sum and product variables
    sum_value = 0
    product_value = 1
    
    # iterate over the list of integers
    for number in numbers:
        sum_value += number
        product_value *= number
    
    # return a tuple consisting of the sum and product of integers
    return sum_value, product_value
