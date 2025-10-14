from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence."""
    if len(numbers) == 0:
        return []
    max_num = numbers[0]
    result = [max_num]
    for i in range(1, len(numbers)):
        if numbers[i] > max_num:
            max_num = numbers[i]
        result.append(max_num)
    return result
