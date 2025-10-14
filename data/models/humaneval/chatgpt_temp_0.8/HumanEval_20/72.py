from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    assert len(numbers) >= 2, "The input list must have at least two elements"
    # Sort the list to make it easier to find the closest elements
    sorted_numbers = sorted(numbers)
    # Initialize the minimum distance to a large value
    min_distance = float("inf")
    # Initialize the closest elements to None
    closest_elements = None
    # Iterate over pairs of adjacent elements in the sorted list
    for i in range(len(sorted_numbers) - 1):
        distance = sorted_numbers[i+1] - sorted_numbers[i]
        # Check if the current pair is closer than the previous closest pair
        if distance < min_distance:
            min_distance = distance
            closest_elements = (sorted_numbers[i], sorted_numbers[i+1])
    # Return the closest elements in order
    return tuple(sorted(closest_elements))
