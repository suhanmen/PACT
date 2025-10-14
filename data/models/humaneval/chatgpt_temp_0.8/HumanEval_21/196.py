python
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given a list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    :param numbers: List of numbers to be rescaled
    :type numbers: List[float]
    :return: List of rescaled numbers
    :rtype: List[float]
    """
    max_num = max(numbers)
    min_num = min(numbers)
    if max_num == min_num:
        return [1.0] * len(numbers)
    return [(x - min_num) / (max_num - min_num) for x in numbers]
