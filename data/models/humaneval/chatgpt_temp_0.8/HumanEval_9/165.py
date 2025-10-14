python
from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Initialize an empty list to store the rolling maximums
    rolling_maxs = []
    
    # Initialize a variable to keep track of the current maximum
    current_max = float('-inf')
    
    # Loop through the numbers and update the rolling maximums
    for num in numbers:
        current_max = max(current_max, num)
        rolling_maxs.append(current_max)
    
    # Return the rolling maximums
    return rolling_maxs
