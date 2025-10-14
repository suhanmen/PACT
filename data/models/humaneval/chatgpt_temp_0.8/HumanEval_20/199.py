from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    n = len(numbers)
    if n < 2:
        raise ValueError("At least two numbers are required")
    numbers.sort()
    min_diff = float("inf")
    closest_pair = None
    for i in range(n - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i + 1])
    return closest_pair
