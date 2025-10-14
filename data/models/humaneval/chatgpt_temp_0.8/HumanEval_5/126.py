from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if len(numbers) <= 1:
        return numbers
    else:
        interspersed = [0] * (2 * len(numbers) - 1)
        interspersed[::2] = numbers
        interspersed[1::2] = [delimeter] * (len(numbers) - 1)
        return interspersed
