from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element
    found until given moment in the sequence.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(max(numbers[:i+1]))
    return result

