from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    interspersed = []
    if len(numbers) == 0:
        return interspersed
    for i in range(len(numbers) - 1):
        interspersed.append(numbers[i])
        interspersed.append(delimeter)
    interspersed.append(numbers[-1])
    return interspersed
