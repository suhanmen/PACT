from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers' """
    new_list = []
    for i in range(len(numbers)):
        if i != 0:
            new_list.append(delimeter)
        new_list.append(numbers[i])
    return new_list
