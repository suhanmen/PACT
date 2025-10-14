from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    assert len(numbers) >= 2, "List must have at least two elements"
    numbers_sorted = sorted(numbers)
    min_diff = float("inf")
    closest_pair = None
    for i in range(len(numbers_sorted) - 1):
        diff = numbers_sorted[i+1] - numbers_sorted[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers_sorted[i], numbers_sorted[i+1])
    return closest_pair
