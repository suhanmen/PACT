python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    res = []
    for i, num in enumerate(numbers):
        if i != 0:
            res.append(delimeter)
        res.append(num)
    return res
