from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()  # sort the list in ascending order
    smallest_diff = float("inf")  # initialize smallest difference as infinity
    closest_pair = (numbers[0], numbers[1])  # initialize closest pair as the first two elements

    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]  # calculate the difference between adjacent elements
        if diff < smallest_diff:
            smallest_diff = diff
            closest_pair = (numbers[i], numbers[i+1])
    
    return closest_pair
