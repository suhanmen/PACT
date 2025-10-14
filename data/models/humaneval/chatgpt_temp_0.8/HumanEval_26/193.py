from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Create an empty set to keep track of unique elements
    unique_numbers = set()
    # Create an empty list to keep track of non-duplicate elements in the same order as input
    non_duplicate_numbers = []
    # Iterate over each number in input list
    for number in numbers:
        # If number is not already in unique_numbers set, add it to both sets
        if number not in unique_numbers:
            unique_numbers.add(number)
            non_duplicate_numbers.append(number)
    # Return the list of non-duplicate numbers in the same order as input
    return non_duplicate_numbers
