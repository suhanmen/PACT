from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    rolling_max_list = [numbers[0]]
    for i in range(1, len(numbers)):
        current_max = max(numbers[:i+1])
        rolling_max_list.append(current_max)
    return rolling_max_list
