python
from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    max_so_far = float('-inf')
    max_list = []
    
    for num in numbers:
        if num > max_so_far:
            max_so_far = num
        max_list.append(max_so_far)
        
    return max_list
