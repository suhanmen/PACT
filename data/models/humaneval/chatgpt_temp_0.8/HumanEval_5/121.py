# CANNOT PARSE CODE SNIPPET
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = []
    for num in numbers[:-1]:
        result.append(num)
        result.append(delimiter)
    if numbers:
        result.append(numbers[-1])
    return result
