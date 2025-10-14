from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()  # sort the list in ascending order
    min_diff = float('inf')  # initialize the minimum difference to infinity
    closest_pair = None  # initialize the closest pair to None
    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]  # calculate the difference between adjacent numbers
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i+1])
    return closest_pair
