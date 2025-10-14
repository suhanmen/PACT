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
    # Create a dictionary to map integer values to roman numerals
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
        1000: 'm'
    }

    # Create a list of integer values in descending order
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    # Initialize an empty string to hold the result
    result = ''

    # Loop through the integer values
    for v in values:
        # While the input number is greater than or equal to the current value
        while number >= v:
            # Add the corresponding roman numeral to the result string
            result += roman_numerals[v]
            # Subtract the current value from the input number
            number -= v

    # Return the result string in lowercase
    return result.lower()
