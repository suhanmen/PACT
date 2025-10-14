from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers = sorted(numbers)
    min_distance = float('inf')
    closest_pair = None
    for i in range(len(numbers) - 1):
        distance = numbers[i+1] - numbers[i]
        if distance < min_distance:
            min_distance = distance
            closest_pair = (numbers[i], numbers[i+1])
    return closest_pair
