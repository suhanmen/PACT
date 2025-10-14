from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    seen = set()
    unique_nums = []
    for num in numbers:
        if num not in seen:
            unique_nums.append(num)
            seen.add(num)
    return unique_nums
