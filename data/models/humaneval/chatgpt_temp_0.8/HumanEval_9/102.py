from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = -float("inf")
    rolling_max_list = []
    for num in numbers:
        max_so_far = max(max_so_far, num)
        rolling_max_list.append(max_so_far)
    return rolling_max_list
