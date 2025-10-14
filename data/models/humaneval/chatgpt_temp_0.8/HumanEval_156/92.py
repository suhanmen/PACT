def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    roman_units = ['', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix']
    roman_tens = ['', 'x', 'xx', 'xxx', 'xl', 'l', 'lx', 'lxx', 'lxxx', 'xc']
    roman_hundreds = ['', 'c', 'cc', 'ccc', 'cd', 'd', 'dc', 'dcc', 'dccc', 'cm']
    roman_thousands = ['', 'm', 'mm', 'mmm']

    if not 1 <= number <= 1000:
        return "Invalid number: out of range"

    roman_numeral = ''

    roman_numeral += roman_thousands[number // 1000]
    roman_numeral += roman_hundreds[(number % 1000) // 100]
    roman_numeral += roman_tens[(number % 100) // 10]
    roman_numeral += roman_units[number % 10]

    return roman_numeral.lower()
