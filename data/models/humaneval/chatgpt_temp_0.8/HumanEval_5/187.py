from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    res = []
    for i in range(len(numbers)-1):
        res.append(numbers[i])
        res.append(delimeter)
    if numbers:
        res.append(numbers[-1])
    return res
