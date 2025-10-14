from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()  # sort the list in ascending order
    closest_pair = (numbers[0], numbers[1])  # initialize with the first two numbers
    min_distance = abs(numbers[0] - numbers[1])  # initialize with the distance between the first two numbers
    for i in range(len(numbers) - 1):
        distance = abs(numbers[i] - numbers[i+1])
        if distance < min_distance:
            closest_pair = (numbers[i], numbers[i+1])
            min_distance = distance
    return closest_pair
