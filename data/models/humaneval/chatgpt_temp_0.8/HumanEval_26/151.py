from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # create an empty set to keep track of unique elements
    unique_nums = set()
    # create an empty list to store non-duplicate elements in the original order
    result = []
    # iterate over the input list
    for num in numbers:
        # if the element is not already in the set, add it to the set and the result list
        if num not in unique_nums:
            unique_nums.add(num)
            result.append(num)
    return result
