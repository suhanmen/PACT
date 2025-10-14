from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    """
    closest_pair = None
    closest_distance = float('inf')
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            distance = abs(numbers[i] - numbers[j])
            if distance < closest_distance:
                closest_pair = (min(numbers[i], numbers[j]), max(numbers[i], numbers[j]))
                closest_distance = distance
    return closest_pair
