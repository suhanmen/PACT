from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    n = len(numbers)
    if n < 2:
        raise ValueError("List must have at least two elements")
    numbers.sort()
    min_distance = float('inf')
    result = None
    for i in range(n - 1):
        distance = numbers[i+1] - numbers[i]
        if distance < min_distance:
            min_distance = distance
            result = (numbers[i], numbers[i+1])
    return result
