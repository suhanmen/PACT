from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    if len(numbers) > 0:
        result.append(numbers[0])
        for i in range(1, len(numbers)):
            result.append(delimeter)
            result.append(numbers[i])
    return result
