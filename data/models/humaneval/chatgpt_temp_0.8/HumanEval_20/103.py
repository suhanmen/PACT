from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers = sorted(numbers)
    best_pair = None
    best_distance = float('inf')
    for i in range(len(numbers) - 1):
        distance = abs(numbers[i] - numbers[i+1])
        if distance < best_distance:
            best_pair = (numbers[i], numbers[i+1])
            best_distance = distance
    return best_pair
