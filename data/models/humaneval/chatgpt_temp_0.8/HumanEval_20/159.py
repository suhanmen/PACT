from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    """
    numbers = sorted(numbers)  # sort the list in ascending order
    closest_diff = float('inf')  # initialize the minimum difference to infinity
    closest_pair = None  # initialize the closest pair to None
    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]  # calculate the difference between adjacent numbers
        if diff < closest_diff:
            closest_diff = diff
            closest_pair = (numbers[i], numbers[i+1])  # update the closest pair
    return closest_pair
