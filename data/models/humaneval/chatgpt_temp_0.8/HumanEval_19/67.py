from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    mapping = {
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
    # Convert the string of numbers to a list of integers
    nums = [mapping[num] for num in numbers.split()]
    # Sort the list of integers
    sorted_nums = sorted(nums)
    # Convert the list of integers back to a string of numbers
    sorted_numbers = ' '.join([num for num, mapping in mapping.items() if mapping in sorted_nums])
    return sorted_numbers
