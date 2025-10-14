from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    numbers.sort()  # sort the list in ascending order
    closest = float('inf')  # start with a very large number
    closest_pair = None
    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]
        if diff < closest:
            closest = diff
            closest_pair = (numbers[i], numbers[i+1])
    return closest_pair
