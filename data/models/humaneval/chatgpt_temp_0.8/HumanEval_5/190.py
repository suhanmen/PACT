# CANNOT PARSE CODE SNIPPET
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list `numbers'
    """
    result = []
    for i in range(len(numbers)-1):
        result.append(numbers[i])
        result.append(delimiter)
    if numbers:
        result.append(numbers[-1])
    return result
