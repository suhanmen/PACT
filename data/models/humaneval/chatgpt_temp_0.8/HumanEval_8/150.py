from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # initialize the sum and product to 0 and 1 respectively
    sum_numbers = 0
    product_numbers = 1
    
    # iterate through the list of numbers
    for number in numbers:
        # update the sum and product accordingly
        sum_numbers += number
        product_numbers *= number
    
    # return the tuple of the sum and product
    return (sum_numbers, product_numbers)
