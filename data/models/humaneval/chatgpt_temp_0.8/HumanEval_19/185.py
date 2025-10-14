from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numeral words from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numerals sorted from smallest to largest
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
    nums = [num_map[num] for num in numbers.split()]
    sorted_nums = sorted(nums)
    sorted_num_words = [list(num_map.keys())[list(num_map.values()).index(num)] for num in sorted_nums]
    return ' '.join(sorted_num_words)
