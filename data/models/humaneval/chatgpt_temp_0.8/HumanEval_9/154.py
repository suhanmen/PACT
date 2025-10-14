from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far = numbers[0] # Initialize the maximum element to the first element of the list
    max_list = [max_so_far] # Create a new list and add the first element as the first rolling maximum
    
    for i in range(1, len(numbers)):
        if numbers[i] > max_so_far:
            max_so_far = numbers[i]
        max_list.append(max_so_far) # Add the maximum element found so far to the new list
    
    return max_list
