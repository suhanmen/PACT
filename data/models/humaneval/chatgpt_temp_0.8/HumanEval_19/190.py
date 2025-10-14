from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    number_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                   'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    # split the input string into a list of numbers
    num_list = numbers.split()
    # convert each number to an integer using the number_dict
    num_list = [number_dict[num] for num in num_list]
    # sort the list of numbers
    num_list.sort()
    # convert each integer back to its corresponding word using the number_dict
    sorted_numbers = [key for key, value in number_dict.items() if value in num_list]
    # join the list of words into a string and return it
    return ' '.join(sorted_numbers)
