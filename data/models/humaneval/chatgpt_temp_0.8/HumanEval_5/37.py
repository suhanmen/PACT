# CANNOT PARSE CODE SNIPPET
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list `numbers'
    """
    output = []
    for i in range(len(numbers)):
        output.append(numbers[i])
        if i != len(numbers) - 1:
            output.append(delimiter)
    return output
