from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    # initialize the minimum difference and the closest pair of numbers
    min_diff = float('inf')
    closest_pair = (None, None)
    # loop through the sorted list of numbers and compare adjacent pairs
    for i in range(len(sorted_numbers) - 1):
        diff = sorted_numbers[i+1] - sorted_numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i+1])
    return closest_pair
