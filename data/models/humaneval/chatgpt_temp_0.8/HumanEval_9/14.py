from typing import List, Tuple

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far = float('-inf') # Initialize the maximum value
    rolling_max_list = [] # Initialize the output list
    for i in range(len(numbers)):
        max_so_far = max(max_so_far, numbers[i]) # Update the maximum value
        rolling_max_list.append(max_so_far) # Append the maximum value to the output list
    return rolling_max_list
