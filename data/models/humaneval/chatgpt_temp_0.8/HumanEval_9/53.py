from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    rolling_max_list = []
    current_max = None
    
    for number in numbers:
        if current_max is None or number > current_max:
            current_max = number
        rolling_max_list.append(current_max)
    
    return rolling_max_list
