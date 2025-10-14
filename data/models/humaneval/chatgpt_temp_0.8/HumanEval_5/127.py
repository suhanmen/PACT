from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    if len(numbers) == 0:
        return result
    for i in range(len(numbers) - 1):
        result.append(numbers[i])
        result.append(delimeter)
    result.append(numbers[-1])
    return result
