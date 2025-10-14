from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for index, number in enumerate(numbers):
        result.append(number)
        if index != len(numbers)-1:
            result.append(delimeter)
    return result
