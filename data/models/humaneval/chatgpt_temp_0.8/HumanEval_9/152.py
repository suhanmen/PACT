from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = []
    current_max = float('-inf')
    for num in numbers:
        current_max = max(current_max, num)
        max_so_far.append(current_max)
    return max_so_far
