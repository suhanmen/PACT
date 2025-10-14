# CANNOT PARSE CODE SNIPPET
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """ Insert a number `delimiter` between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result = []
    for i in range(len(numbers)):
        if i == len(numbers) - 1:
            result.append(numbers[i])
        else:
            result.append(numbers[i])
            result.append(delimiter)
    return result
