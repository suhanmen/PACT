from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    rolling_max_list = []
    max_so_far = 0
    for num in numbers:
        if num > max_so_far:
            max_so_far = num
        rolling_max_list.append(max_so_far)
    return rolling_max_list
