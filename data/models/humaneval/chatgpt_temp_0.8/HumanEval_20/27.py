from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()  # sort the list in ascending order
    min_diff = float('inf')
    min_pair = (0.0, 0.0)
    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            min_pair = (numbers[i], numbers[i+1])
    return min_pair
