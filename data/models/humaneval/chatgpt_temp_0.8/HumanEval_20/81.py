python
from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    min_distance = float('inf')
    closest_pair = None
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            distance = abs(numbers[i] - numbers[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (min(numbers[i], numbers[j]), max(numbers[i], numbers[j]))
    return closest_pair
