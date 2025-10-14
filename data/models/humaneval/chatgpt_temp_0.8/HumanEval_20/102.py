from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()  # sort the list of numbers in ascending order
    min_diff = float('inf')  # initialize the minimum difference to infinity
    closest_pair = None  # initialize the closest pair to None

    # iterate through the list of numbers, comparing adjacent pairs
    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]  # calculate the difference between the current pair
        if diff < min_diff:  # if the difference is smaller than the current minimum difference
            min_diff = diff  # update the minimum difference
            closest_pair = (numbers[i], numbers[i+1])  # update the closest pair

    return closest_pair  # return the closest pair, in order
