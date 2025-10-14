# CANNOT PARSE CODE SNIPPET
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:
        return []
    result = [numbers[0]]
    for num in numbers[1:]:
        result.append(delimiter)
        result.append(num)
    return result
