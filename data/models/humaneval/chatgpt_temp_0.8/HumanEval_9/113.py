python
from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = float('-inf')
    max_list = []
    for num in numbers:
        max_so_far = max(num, max_so_far)
        max_list.append(max_so_far)
    return max_list
