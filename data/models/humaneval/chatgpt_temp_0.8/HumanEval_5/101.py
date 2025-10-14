from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers' """
    result = []
    for i, n in enumerate(numbers[:-1]):
        result.extend([n, delimeter])
    if numbers:
        result.append(numbers[-1])
    return result
