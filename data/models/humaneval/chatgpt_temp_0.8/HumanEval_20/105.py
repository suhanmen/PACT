from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()
    smallest_difference = abs(numbers[1] - numbers[0])
    closest = (numbers[0], numbers[1])
    for i in range(1, len(numbers) - 1):
        difference = abs(numbers[i + 1] - numbers[i])
        if difference < smallest_difference:
            smallest_difference = difference
            closest = (numbers[i], numbers[i + 1])
    return closest
