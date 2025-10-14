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
    # Define Roman numeral symbols and their corresponding values
    roman_symbols = {
        1: "i",
        4: "iv",
        5: "v",
        9: "ix",
        10: "x",
        40: "xl",
        50: "l",
        90: "xc",
        100: "c",
        400: "cd",
        500: "d",
        900: "cm",
        1000: "m"
    }

    # Initialize result string
    roman_numeral = ""

    # Loop through the roman symbols in descending order
    for value, symbol in sorted(roman_symbols.items(), reverse=True):
        # Add as many symbols as possible to the result string
        while number >= value:
            roman_numeral += symbol
            number -= value

    return roman_numeral.lower()
