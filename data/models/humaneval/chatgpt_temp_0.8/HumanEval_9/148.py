from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = float('-inf')
    rolling_maxes = []
    for num in numbers:
        max_so_far = max(num, max_so_far)
        rolling_maxes.append(max_so_far)
    return rolling_maxes
