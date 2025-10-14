from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    sorted_numbers = sorted(numbers)
    min_distance = float("inf")
    closest_pair = ()
    for i in range(len(sorted_numbers)-1):
        distance = abs(sorted_numbers[i+1] - sorted_numbers[i])
        if distance < min_distance:
            min_distance = distance
            closest_pair = (sorted_numbers[i], sorted_numbers[i+1])
    return closest_pair
