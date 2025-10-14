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
    # Define the mapping between integers and roman numerals
    roman_map = {
        1: 'i',
        4: 'iv',
        5: 'v',
        9: 'ix',
        10: 'x',
        40: 'xl',
        50: 'l',
        90: 'xc',
        100: 'c',
        400: 'cd',
        500: 'd',
        900: 'cm',
        1000: 'm'
    }

    # Create a list of tuples with the decimal values and corresponding roman numerals
    roman_pairs = sorted(roman_map.items(), reverse=True)

    # Convert the integer to roman numerals
    roman_digits = []
    for value, numeral in roman_pairs:
        while number >= value:
            roman_digits.append(numeral)
            number -= value

    # Return the string with the lowercase roman numerals
    return ''.join(roman_digits).lower()
