from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers_sorted = sorted(numbers)  # sort the list in ascending order
    min_diff = float("inf")  # set the minimum difference to infinity
    closest_pair = None  # initialize the closest pair to None
    for i in range(len(numbers_sorted) - 1):  # iterate over all adjacent pairs
        diff = numbers_sorted[i+1] - numbers_sorted[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers_sorted[i], numbers_sorted[i+1])
    return closest_pair
