from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort() # Sort the list of numbers in ascending order
    closest_pair = (numbers[0], numbers[1]) # Initialize the closest pair to the first two elements
    closest_distance = abs(numbers[0] - numbers[1]) # Initialize the closest distance to the distance between the first two elements

    # Iterate through the list of numbers, comparing each pair of adjacent elements
    for i in range(len(numbers) - 1):
        distance = abs(numbers[i] - numbers[i+1])
        if distance < closest_distance:
            closest_pair = (numbers[i], numbers[i+1])
            closest_distance = distance

    return closest_pair
