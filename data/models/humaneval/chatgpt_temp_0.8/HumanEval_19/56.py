from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    
    number_dict = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4,
                   'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    # Convert string of words to list of integers
    nums = [number_dict[num] for num in numbers.split()]
    
    # Sort the list of integers
    nums.sort()
    
    # Convert list of integers back to string of words
    words = [key for key, value in number_dict.items() if value in nums]
    return ' '.join(words)
