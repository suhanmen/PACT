from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far = float('-inf') # set initial maximum to negative infinity
    max_list = [] # create an empty list to store the maximums
    for num in numbers:
        max_so_far = max(max_so_far, num) # update maximum if current number is greater
        max_list.append(max_so_far) # append the maximum to the list
    return max_list
