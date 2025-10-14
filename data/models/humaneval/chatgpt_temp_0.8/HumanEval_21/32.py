from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_num = min(numbers)
    max_num = max(numbers)
    rescaled = []
    for num in numbers:
        rescaled_num = (num - min_num) / (max_num - min_num)
        rescaled.append(rescaled_num)
    return rescaled
