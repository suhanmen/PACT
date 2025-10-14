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
    # Split the input string into a list of numbers
    num_list = numbers.split()
    # Convert each number from string to integer using the dictionary
    # to look up the corresponding integer value
    num_list = [num_dict[num] for num in num_list]
    # Sort the list of integers in ascending order
    num_list.sort()
    # Convert the sorted list back to a string, replacing integers with their string equivalents
    sorted_numbers = [list(num_dict.keys())[list(num_dict.values()).index(num)] for num in num_list]
    return ' '.join(sorted_numbers)
