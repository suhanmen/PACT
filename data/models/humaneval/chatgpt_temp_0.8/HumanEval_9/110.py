from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    result = []
    maximum = float('-inf')
    for number in numbers:
        maximum = max(maximum, number)
        result.append(maximum)
    return result
