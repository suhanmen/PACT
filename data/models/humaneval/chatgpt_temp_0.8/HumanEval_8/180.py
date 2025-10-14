from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    # Initialize sum and product to 0 and 1, respectively
    sum_nums = 0
    product_nums = 1
    
    # Loop through each number in the list and update sum and product accordingly
    for num in numbers:
        sum_nums += num
        product_nums *= num
        
    # Return a tuple of the sum and product
    return (sum_nums, product_nums)
