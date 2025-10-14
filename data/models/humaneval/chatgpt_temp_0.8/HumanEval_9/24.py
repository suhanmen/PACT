from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_list = []  # create an empty list to store the rolling maximums
    current_max = float('-inf')  # set the current maximum to negative infinity
    
    for number in numbers:
        if number > current_max:
            current_max = number
        max_list.append(current_max)
        
    return max_list
