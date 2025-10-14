from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Create a dictionary to keep track of the frequency of each number
    freq = {}
    
    # Iterate over the input list and update the frequency dictionary
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    
    # Create a new list to collect the non-duplicate elements
    result = []
    
    # Iterate over the input list again and add each non-duplicate element to the result list
    for num in numbers:
        if freq[num] == 1:
            result.append(num)
            freq[num] = 0  # Mark the element as added to result
    
    return result
