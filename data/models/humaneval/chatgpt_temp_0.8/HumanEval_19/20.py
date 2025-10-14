NUMERAL_TO_DIGIT = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    numerals = numbers.split()
    digits = [NUMERAL_TO_DIGIT[numeral] for numeral in numerals]
    digits.sort()
    sorted_numerals = [key for key, value in NUMERAL_TO_DIGIT.items() if value in digits]
    sorted_numbers = ' '.join(sorted_numerals)
    return sorted_numbers
