from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    # initialize sum and product to 0 and 1 respectively
    sum = 0
    product = 1
    # loop through the list of numbers
    for number in numbers:
        # add the current number to the sum
        sum += number
        # multiply the current number to the product
        product *= number
    # return a tuple consisting of the sum and product
    return (sum, product)
