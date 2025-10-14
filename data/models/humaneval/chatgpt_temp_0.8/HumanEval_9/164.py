from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    max_numbers = []
    max_num = None
    for num in numbers:
        if max_num is None or num > max_num:
            max_num = num
        max_numbers.append(max_num)
    return max_numbers
