from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number)."""

    numbers = sorted(numbers)
    diff = [abs(numbers[i] - numbers[i+1]) for i in range(len(numbers)-1)]
    min_index = diff.index(min(diff))
    return (numbers[min_index], numbers[min_index+1])
