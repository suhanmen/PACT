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
    min_diff = float('inf')  # initialize the minimum difference to infinity
    min_pair = (None, None)  # initialize the minimum pair to None
    
    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]  # calculate the difference between adjacent numbers
        if diff < min_diff:
            min_diff = diff
            min_pair = (numbers[i], numbers[i+1])  # update the minimum pair
    
    return min_pair
