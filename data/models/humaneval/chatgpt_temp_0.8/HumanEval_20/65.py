from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    closest_pair = None
    min_distance = float('inf')
    for i in range(len(numbers) - 1):
        distance = numbers[i+1] - numbers[i]
        if distance < min_distance:
            closest_pair = (numbers[i], numbers[i+1])
            min_distance = distance
    return closest_pair
