from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numbers_dict = {
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
    numbers_list = numbers.split()
    # Convert the list of numbers to a list of integers by looking up each number in the dictionary
    numbers_ints = [numbers_dict[num] for num in numbers_list]
    # Sort the list of integers
    numbers_ints.sort()
    # Convert the list of integers back to a list of strings by looking up each integer in the dictionary
    numbers_sorted = [num for num, val in numbers_dict.items() if val in numbers_ints]
    # Join the list of sorted strings into a single, space-delimited string
    return ' '.join(numbers_sorted)
