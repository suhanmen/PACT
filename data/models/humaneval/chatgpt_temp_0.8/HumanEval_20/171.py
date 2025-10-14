from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # sort the list in ascending order
    numbers.sort()
    # set up variables to hold the closest pair and their difference
    closest_pair = (numbers[0], numbers[1])
    min_diff = numbers[1] - numbers[0]
    # iterate through the list and compare adjacent elements
    for i in range(1, len(numbers) - 1):
        diff = numbers[i + 1] - numbers[i]
        if diff < min_diff:
            closest_pair = (numbers[i], numbers[i + 1])
            min_diff = diff
    return closest_pair
