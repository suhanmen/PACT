from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Create an empty list to store unique elements
    unique_nums = []
    # Iterate through each element in the input list
    for num in numbers:
        # If the element is not already in the unique list, add it
        if num not in unique_nums:
            unique_nums.append(num)
    # Return the list of unique elements
    return unique_nums
