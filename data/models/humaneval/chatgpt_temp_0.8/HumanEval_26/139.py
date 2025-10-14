from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Create an empty list to hold the unique numbers
    unique_numbers = []
    
    # Loop through each number in the input list
    for number in numbers:
        # If the number hasn't been seen before, add it to the unique_numbers list
        if number not in unique_numbers:
            unique_numbers.append(number)
    
    # Return the list of unique numbers
    return unique_numbers
