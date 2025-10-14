from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).

    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    sorted_numbers = sorted(numbers)  # sort the numbers list in ascending order
    min_diff = float('inf')  # initialize the minimum difference to infinity
    closest_pair = None  # initialize the closest pair to None
    for i in range(len(sorted_numbers) - 1):
        diff = sorted_numbers[i+1] - sorted_numbers[i]  # calculate the difference between adjacent numbers
        if diff < min_diff:
            min_diff = diff  # update the minimum difference
            closest_pair = (sorted_numbers[i], sorted_numbers[i+1])  # update the closest pair
    return closest_pair  # return the closest pair as a tuple
