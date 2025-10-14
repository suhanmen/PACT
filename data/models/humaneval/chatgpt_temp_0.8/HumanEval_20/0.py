from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # sort the numbers in ascending order
    numbers.sort()
    # initialize the minimum difference and the corresponding pair of numbers
    min_diff = float('inf')
    closest_pair = None
    # iterate through all adjacent pairs of numbers and update the minimum difference if necessary
    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i+1])
    return closest_pair
