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

    # Define the mappings for the roman numerals and their values.
    roman_numerals = {
        1000: 'm',
        900: 'cm',
        500: 'd',
        400: 'cd',
        100: 'c',
        90: 'xc',
        50: 'l',
        40: 'xl',
        10: 'x',
        9: 'ix',
        5: 'v',
        4: 'iv',
        1: 'i'
    }

    # Create an empty string to store the result.
    result = ""

    # Iterate through the roman numerals and their values, starting with the highest value.
    for value, numeral in roman_numerals.items():
        # If the number is greater than or equal to the value, add the corresponding numeral to the result.
        while number >= value:
            result += numeral
            # Subtract the value from the number.
            number -= value

    # Return the result in lowercase.
    return result.lower()
