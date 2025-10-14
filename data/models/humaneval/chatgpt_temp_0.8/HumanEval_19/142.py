from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    num_map = {
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
    # Convert each number to its numerical value using the num_map
    num_list = [num_map[num] for num in num_list]
    # Sort the numerical values
    num_list.sort()
    # Convert the numerical values back to their string representations
    sorted_numbers = [list(num_map.keys())[list(num_map.values()).index(num)] for num in num_list]
    # Join the sorted numbers back into a space-delimited string
    return ' '.join(sorted_numbers)
