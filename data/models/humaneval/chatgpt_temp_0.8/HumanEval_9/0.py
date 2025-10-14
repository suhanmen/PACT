from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_numbers = []  # create an empty list to store the rolling maximum numbers
    current_max = None  # create a variable to store the current maximum number
    
    for number in numbers:
        if current_max is None or number > current_max:
            current_max = number  # update the current maximum number if the current number is greater
        max_numbers.append(current_max)  # add the current maximum number to the list of rolling maximum numbers
        
    return max_numbers  # return the list of rolling maximum numbers
