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
    
    # Initialize sum and product variables
    sum_of_numbers = 0
    product_of_numbers = 1
    
    # Iterate through the list of numbers
    for number in numbers:
        # Add the number to the sum
        sum_of_numbers += number
        # Multiply the number to the product
        product_of_numbers *= number
    
    # Return the sum and product as a tuple
    return (sum_of_numbers, product_of_numbers)
