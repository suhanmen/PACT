from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers_sorted = sorted(numbers)
    closest_pair = (numbers_sorted[0], numbers_sorted[1])
    smallest_difference = numbers_sorted[1] - numbers_sorted[0]
    for i in range(1, len(numbers_sorted)-1):
        current_difference = numbers_sorted[i+1] - numbers_sorted[i]
        if current_difference < smallest_difference:
            smallest_difference = current_difference
            closest_pair = (numbers_sorted[i], numbers_sorted[i+1])
    return closest_pair
