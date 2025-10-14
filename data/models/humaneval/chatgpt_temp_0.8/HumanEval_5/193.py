from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    interspersed = []
    for num in numbers[:-1]:
        interspersed.extend([num, delimeter])
    if numbers:
        interspersed.append(numbers[-1])
    return interspersed
