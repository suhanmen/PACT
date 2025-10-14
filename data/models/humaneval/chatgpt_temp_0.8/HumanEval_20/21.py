from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    """
    numbers.sort()
    closest = numbers[1] - numbers[0]
    closest_pair = (numbers[0], numbers[1])
    for i in range(1, len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]
        if diff < closest:
            closest = diff
            closest_pair = (numbers[i], numbers[i+1])
    return closest_pair
