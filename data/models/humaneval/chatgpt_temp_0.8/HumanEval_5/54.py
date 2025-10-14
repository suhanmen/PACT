from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'"""
    result = []
    for num in numbers[:-1]:
        result += [num, delimeter]
    if numbers:
        result.append(numbers[-1])
    return result
    
