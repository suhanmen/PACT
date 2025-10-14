python
from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers = sorted(numbers)  # sort the list of numbers in ascending order
    closest_pair = (numbers[0], numbers[1])  # initialize closest_pair with first two numbers
    min_distance = numbers[1] - numbers[0]  # initialize min_distance with the distance between first two numbers
    for i in range(1, len(numbers) - 1):
        distance = numbers[i + 1] - numbers[i]  # calculate the distance between current two numbers
        if distance < min_distance:
            min_distance = distance  # update min_distance if a smaller distance is found
            closest_pair = (numbers[i], numbers[i + 1])  # update closest_pair with current two numb
