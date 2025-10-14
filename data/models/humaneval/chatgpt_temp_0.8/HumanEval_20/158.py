from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()  # sort the numbers in ascending order
    closest_pair = (numbers[0], numbers[1])  # initialize closest pair as the first two numbers
    closest_distance = abs(numbers[1] - numbers[0])  # initialize closest distance as the difference between first two numbers
    
    # Check distances between adjacent pairs of numbers
    for i in range(1, len(numbers) - 1):
        distance = abs(numbers[i+1] - numbers[i])
        if distance < closest_distance:
            closest_distance = distance
            closest_pair = (numbers[i], numbers[i+1])
    
    return closest_pair
