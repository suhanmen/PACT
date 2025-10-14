from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in the list.
    The empty sum should be equal to 0 and the empty product should be equal to 1.
    """
    if not numbers: # if the list is empty
        return 0, 1 # return 0 for sum and 1 for product
    
    # initialize the sum and product variables
    sum_ = 0
    product = 1
    
    for num in numbers:
        sum_ += num # add the number to the sum
        product *= num # multiply the number to the product
    
    # return the sum and product as a tuple
    return sum_, product
