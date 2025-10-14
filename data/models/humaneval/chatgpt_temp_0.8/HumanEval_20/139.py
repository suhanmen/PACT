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
    closest = float('inf')  # set a variable to track the closest difference found
    result = None  # initialize the result to None
    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]  # calculate the difference between adjacent numbers
        if diff < closest:
            closest = diff  # update closest if a smaller difference is found
            result = (numbers[i], numbers[i+1])  # update the result with the new closest pair
    return result
