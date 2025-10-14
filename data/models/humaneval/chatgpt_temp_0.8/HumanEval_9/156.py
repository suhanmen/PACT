python
from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_list = []  # To store the rolling maximum elements
    max_elem = float('-inf')  # Initialize the maximum element to be negative infinity
    
    for num in numbers:
        if num > max_elem:
            max_elem = num
        max_list.append(max_elem)
    
    return max_list
