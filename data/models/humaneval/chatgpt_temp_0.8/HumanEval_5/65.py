# CANNOT PARSE CODE SNIPPET
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list `numbers'
    """
    if len(numbers) == 0:
        return []
    result = [numbers[0]]
    for i in range(1, len(numbers)):
        result.append(delimiter)
        result.append(numbers[i])
    return result
