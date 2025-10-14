from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    """
    numbers = sorted(numbers)
    closest_distance = float('inf')
    closest_pair = None
    for i in range(len(numbers) - 1):
        distance = numbers[i+1] - numbers[i]
        if distance < closest_distance:
            closest_distance = distance
            closest_pair = (numbers[i], numbers[i+1])
    return closest_pair
