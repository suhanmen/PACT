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
    # Define a mapping of integers to Roman numerals
    roman_numerals = {
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
        1000: 'm',
    }

    # Initialize an empty string to store the Roman numeral
    roman_numeral = ""

    # Iterate through the mapping of integers to Roman numerals
    for numeral, value in sorted(roman_numerals.items(), reverse=True):
        # Determine how many times the numeral should be used
        count = number // numeral
        # Add the appropriate number of Roman numeral characters to the result
        roman_numeral += value * count
        # Update the number to account for the Roman numerals used so far
        number -= numeral * count

    # Return the result
    return roman_numeral.lower()
