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
    # Define a dictionary of Roman numeral symbols and their values
    roman_numerals = {
        1000: 'm', 900: 'cm', 500: 'd', 400: 'cd',
        100: 'c', 90: 'xc', 50: 'l', 40: 'xl',
        10: 'x', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'
    }
    # Initialize an empty string to hold the mini Roman numeral representation
    mini_roman = ''
    # Loop through the dictionary keys in descending order
    for value, symbol in sorted(roman_numerals.items(), reverse=True):
        # Subtract the largest possible multiple of the value from the given number
        while number >= value:
            mini_roman += symbol
            number -= value
    # Return the mini Roman numeral representation as a lowercase string
    return mini_roman.lower()
