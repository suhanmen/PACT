from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = 0
    result = []
    for i in range(len(numbers)):
        max_so_far = max(max_so_far, numbers[i])
        result.append(max_so_far)
    return result
