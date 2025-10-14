python
from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_so_far = []
    window = []
    for number in numbers:
        window.append(number)
        max_so_far.append(max(window))
        if len(window) > 3:
            window.pop(0)
    return max_so_far
