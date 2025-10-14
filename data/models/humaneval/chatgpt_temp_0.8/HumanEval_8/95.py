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

    # Initialize sum and product to the first element in the list
    sum_numbers = numbers[0]
    product_numbers = numbers[0]

    # Iterate through the list and update the sum and product
    for number in numbers[1:]:
        sum_numbers += number
        product_numbers *= number

    return sum_numbers, product_numbers
