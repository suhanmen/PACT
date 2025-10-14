from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Initialize an empty list to store the rolling maximum values
    max_numbers = []
    
    # Initialize a variable to keep track of the maximum value seen so far
    max_so_far = None
    
    # Iterate through the list of numbers
    for num in numbers:
        # If the maximum value seen so far is None or the current number is greater than the maximum value,
        # update the maximum value to the current number
        if max_so_far is None or num > max_so_far:
            max_so_far = num
        
        # Append the current maximum value to the max_numbers list
        max_numbers.append(max_so_far)
    
    return max_numbers
