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

    # Dictionary containing the roman numeral symbols and their values
    roman_dict = {
        1000: 'm', 900: 'cm', 500: 'd', 400: 'cd', 100: 'c', 90: 'xc',
        50: 'l', 40: 'xl', 10: 'x', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'
    }

    # Initialize an empty string to store the roman numeral
    roman_numeral = ""

    # Loop through the roman numeral symbols and their values, adding them to the string
    for value, symbol in roman_dict.items():
        while number >= value:
            roman_numeral += symbol
            number -= value

    # Return the lowercase roman numeral string
    return roman_numeral.lower()
