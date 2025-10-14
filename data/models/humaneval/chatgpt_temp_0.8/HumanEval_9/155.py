from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    rolling_max_list = []
    max_so_far = None
    
    for num in numbers:
        if max_so_far is None or num > max_so_far:
            max_so_far = num
        
        rolling_max_list.append(max_so_far)
    
    return rolling_max_list
