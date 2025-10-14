from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the input list in ascending order
    numbers.sort()
    # Initialize the minimum difference and the two closest numbers
    min_diff = float('inf')
    closest_nums = (0.0, 0.0)
    # Iterate over the list and compare adjacent pairs of numbers
    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_nums = (numbers[i], numbers[i+1])
    return closest_nums
