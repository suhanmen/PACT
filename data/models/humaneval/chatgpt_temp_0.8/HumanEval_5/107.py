from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimeter' between every two consecutive elements of input list `numbers'"""
    new_list = []
    for i in range(len(numbers)):
        new_list.append(numbers[i])
        if i != len(numbers) - 1:
            new_list.append(delimeter)
    return new_list
