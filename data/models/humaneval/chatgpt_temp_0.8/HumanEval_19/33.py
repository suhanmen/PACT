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
    # Convert the list of numberals to a list of integers based on the num_dict
    num_int = [num_dict[num] for num in num_list]
    # Sort the list of integers in ascending order
    sorted_num = sorted(num_int)
    # Convert the list of sorted integers back to numberals based on the num_dict
    sorted_numeral = [list(num_dict.keys())[list(num_dict.values()).index(num)] for num in sorted_num]
    # Join the sorted numberals back into a string and return it
    return ' '.join(sorted_numeral)
