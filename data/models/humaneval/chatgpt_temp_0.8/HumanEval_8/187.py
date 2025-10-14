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
    if not numbers:  # if the list is empty
        return 0, 1  # return 0 for the sum and 1 for the product
    else:
        sum_of_numbers = sum(numbers)  # sum of all the numbers in the list
        product_of_numbers = 1  # initialize the product as 1
        for number in numbers:
            product_of_numbers *= number  # calculate the product of all the numbers
        return sum_of_numbers, product_of_numbers
