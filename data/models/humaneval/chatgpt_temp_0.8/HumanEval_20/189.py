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
    min_diff = float('inf')  # set the minimum difference to infinity
    closest_nums = ()  # initialize a tuple to store the closest numbers

    # loop through the list of numbers and calculate the difference between adjacent numbers
    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]

        # check if the calculated difference is smaller than the current minimum difference
        if diff < min_diff:
            min_diff = diff
            closest_nums = (numbers[i], numbers[i+1])

    return closest_nums
