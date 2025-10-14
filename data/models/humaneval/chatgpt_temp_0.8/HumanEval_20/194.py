from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # sort the list of numbers
    numbers.sort()
    # initialize variables for the closest numbers and their difference
    closest_pair = (numbers[0], numbers[1])
    closest_diff = abs(numbers[0] - numbers[1])
    # loop through the list of numbers, comparing adjacent pairs
    for i in range(len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i+1])
        if diff < closest_diff:
            closest_pair = (numbers[i], numbers[i+1])
            closest_diff = diff
    return closest_pair
