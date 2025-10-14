from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = float('-inf')
    results = []
    for num in numbers:
        max_so_far = max(max_so_far, num)
        results.append(max_so_far)
    return results
