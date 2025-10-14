from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    """
    if not numbers:
        return 0, 1
    else:
        s = sum(numbers)
        p = 1
        for n in numbers:
            p *= n
        return s, p
