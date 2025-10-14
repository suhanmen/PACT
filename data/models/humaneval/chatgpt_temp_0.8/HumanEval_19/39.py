from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    num_dict = {
        'zero': 0, 
        'one': 1, 
        'two': 2, 
        'three': 3, 
        'four': 4, 
        'five': 5, 
        'six': 6, 
        'seven': 7, 
        'eight': 8,
        'nine': 9
    }
    # Split the input string into a list of individual numbers
    num_list = numbers.split()
    # Convert the list of words to a list of numbers
    num_list = [num_dict[num] for num in num_list]
    # Sort the list of numbers
    num_list.sort()
    # Convert the list of numbers back to a list of words
    num_list = [list(num_dict.keys())[list(num_dict.values()).index(num)] for num in num_list]
    # Join the list of words to form the final string
    return ' '.join(num_list)
