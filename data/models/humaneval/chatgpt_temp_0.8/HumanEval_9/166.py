from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence. """
    max_numbers = []
    current_max = float("-inf")
    for i in range(len(numbers)):
        if numbers[i] > current_max:
            current_max = numbers[i]
        max_numbers.append(current_max)
    return max_numbers
