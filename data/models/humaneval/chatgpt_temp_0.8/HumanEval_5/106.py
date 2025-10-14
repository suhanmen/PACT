from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimeter' between every two consecutive elements of input list `numbers'"""
    new_list = []
    for i in range(len(numbers)-1):
        new_list.append(numbers[i])
        new_list.append(delimeter)
    if numbers:
        new_list.append(numbers[-1])
    return new_list
