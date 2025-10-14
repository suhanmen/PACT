from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_num = float('-inf')
    max_nums = []
    for num in numbers:
        if num > max_num:
            max_num = num
        max_nums.append(max_num)
    return max_nums
