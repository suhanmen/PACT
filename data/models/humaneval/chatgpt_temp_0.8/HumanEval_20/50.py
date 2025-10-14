from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two numbers.")
    numbers.sort()
    closest_pair = (numbers[0], numbers[1])
    min_distance = abs(numbers[1] - numbers[0])
    for i in range(1, len(numbers) - 1):
        dist = abs(numbers[i+1] - numbers[i])
        if dist < min_distance:
            closest_pair = (numbers[i], numbers[i+1])
            min_distance = dist
    return closest_pair
