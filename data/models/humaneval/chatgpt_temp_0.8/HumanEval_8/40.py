python
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # Initialize variables for sum and product
    s, p = 0, 1
    
    # Compute sum and product
    for num in numbers:
        s += num
        p *= num
    
    # Return the sum and product as a tuple
    return s, p if numbers else (0, 1)
