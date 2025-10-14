# CANNOT PARSE CODE SNIPPET
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list `numbers'
    """
    new_list = []
    for i in range(len(numbers)):
        if i == len(numbers) - 1:
            new_list.append(numbers[i])
        else:
            new_list.append(numbers[i])
            new_list.append(delimiter)
    return new_list
