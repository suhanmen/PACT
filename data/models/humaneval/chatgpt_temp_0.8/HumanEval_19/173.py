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

INT_TO_NUMERAL = {v: k for k, v in NUMERAL_TO_INT.items()}

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    split_numbers = numbers.split()
    int_numbers = [NUMERAL_TO_INT[numeral] for numeral in split_numbers]
    sorted_int_numbers = sorted(int_numbers)
    sorted_numerals = [INT_TO_NUMERAL[num] for num in sorted_int_numbers]
    return ' '.join(sorted_numerals)
