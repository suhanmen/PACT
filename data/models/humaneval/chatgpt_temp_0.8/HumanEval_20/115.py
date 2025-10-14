from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Check that the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    # Sort the list in ascending order
    numbers.sort()

    # Initialize variables to keep track of the closest pair of numbers
    closest_pair = (numbers[0], numbers[1])
    closest_distance = abs(numbers[0] - numbers[1])

    # Iterate over the list and compare adjacent pairs of numbers
    for i in range(len(numbers) - 1):
        distance = abs(numbers[i] - numbers[i+1])
        if distance < closest_distance:
            closest_pair = (numbers[i], numbers[i+1])
            closest_distance = distance

    return closest_pair
