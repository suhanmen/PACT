# CANNOT PARSE CODE SNIPPET
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    interspersed = []
    for i in range(len(numbers)):
        interspersed.append(numbers[i])
        if i != len(numbers) - 1:
            interspersed.append(delimiter)
    return interspersed
