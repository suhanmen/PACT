from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    sorted_numbers = sorted(numbers)
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    smallest_distance = sorted_numbers[1] - sorted_numbers[0]
    for i in range(1, len(sorted_numbers) - 1):
        distance = sorted_numbers[i+1] - sorted_numbers[i]
        if distance < smallest_distance:
            smallest_distance = distance
            closest_pair = (sorted_numbers[i], sorted_numbers[i+1])
    return closest_pair
