from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    sum_result = 0
    product_result = 1
    
    if len(numbers) == 0:
        return sum_result, product_result
    
    for number in numbers:
        sum_result += number
        product_result *= number
    
    return sum_result, product_result
