from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'"""
    result = []
    for i in range(len(numbers)):
        if i != 0:
            result.append(delimeter)
        result.append(numbers[i])
    return result
