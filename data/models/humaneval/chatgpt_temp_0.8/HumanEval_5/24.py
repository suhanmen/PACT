# CANNOT PARSE CODE SNIPPET
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list `numbers' """
    interspersed = []
    for num in numbers[:-1]:
        interspersed.extend([num, delimiter])
    if numbers:
        interspersed.append(numbers[-1])
    return interspersed
