from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # Initialize the sum and product variables
    sum_num = 0
    product_num = 1
    
    # Calculate the sum and product of the given numbers
    for num in numbers:
        sum_num += num
        product_num *= num
    
    # Return the tuple of the sum and product
    return (sum_num, product_num)
