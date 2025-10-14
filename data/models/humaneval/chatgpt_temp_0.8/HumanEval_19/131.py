NUMERAL_TO_INT = {
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

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    nums = [NUMERAL_TO_INT[num] for num in numbers.split()]
    sorted_nums = sorted(nums)
    sorted_numeral_strs = [list(NUMERAL_TO_INT.keys())[list(NUMERAL_TO_INT.values()).index(num)] for num in sorted_nums]
    return ' '.join(sorted_numeral_strs)
