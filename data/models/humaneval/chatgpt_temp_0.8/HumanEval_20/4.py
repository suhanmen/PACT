from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    n = len(numbers)
    assert n >= 2, "numbers must have at least two elements"
    numbers.sort()
    min_diff = float("inf")
    result = None
    for i in range(n - 1):
        diff = numbers[i+1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            result = (numbers[i], numbers[i+1])
    return result
