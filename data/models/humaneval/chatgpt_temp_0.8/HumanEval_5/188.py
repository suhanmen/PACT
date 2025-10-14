from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    res = []
    for i in range(len(numbers)):
        if i != 0:
            res.append(delimeter)
        res.append(numbers[i])
    return res
