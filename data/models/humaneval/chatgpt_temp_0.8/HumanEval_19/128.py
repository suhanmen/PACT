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
    # split string by space and convert each word to its corresponding number
    numbers_lst = [number_dict[num] for num in numbers.split()]
    # sort the numbers
    numbers_lst.sort()
    # convert numbers back to words and join them with a space
    return ' '.join([key for key, value in number_dict.items() if value in numbers_lst])
