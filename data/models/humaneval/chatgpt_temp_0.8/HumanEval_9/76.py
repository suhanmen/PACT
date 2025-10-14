from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = numbers[0]
    rolling_max = [max_so_far]
    for i in range(1, len(numbers)):
        if numbers[i] > max_so_far:
            max_so_far = numbers[i]
        rolling_max.append(max_so_far)
    return rolling_max
