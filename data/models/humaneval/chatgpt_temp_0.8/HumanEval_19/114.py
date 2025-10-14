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
    # Split the string into a list of number strings
    num_list = numbers.split()
    # Convert each number string to an integer using the num_dict
    num_list = [num_dict[num] for num in num_list]
    # Sort the list of integers
    num_list.sort()
    # Convert the sorted list of integers back to number strings using the num_dict
    sorted_num_list = [list(num_dict.keys())[list(num_dict.values()).index(num)] for num in num_list]
    # Join the sorted number strings back into a space-delimited string
    sorted_numbers = ' '.join(sorted_num_list)
    return sorted_numbers
