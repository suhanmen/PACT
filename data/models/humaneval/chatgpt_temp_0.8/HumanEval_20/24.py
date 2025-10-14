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
    closest_pair = (numbers[0], numbers[1])  # initialize closest_pair with the first two elements of the sorted list
    min_distance = abs(numbers[0] - numbers[1])  # initialize min_distance with the absolute difference between the first two elements of the sorted list
    for i in range(1, len(numbers) - 1):  # iterate over the sorted list (excluding the first and last elements)
        distance = abs(numbers[i] - numbers[i+1])  # calculate the distance between the current element and the next element
        if distance < min_distance:  # if the current distance is less than the current minimum distance
            min_distance = distance  # update the minimum distance
            closest_pair = (numbers[i], numbers[i+1])  # update the closest pair with the current pair of elements
    return closest_pair  # return the closest pair of elements
