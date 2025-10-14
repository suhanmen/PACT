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
    # Roman numeral symbols and their values
    roman_symbols = {
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
    
    # Initialize an empty string to store the resulting roman numeral
    roman_numeral = ""
    
    # Loop through the roman symbols and their values
    for value, symbol in roman_symbols.items():
        
        # Divide the number by the value, and add the corresponding symbol
        # to the roman numeral string that many times
        count = int(number / value)
        roman_numeral += symbol * count
        
        # Subtract the value times the count from the number
        number -= value * count
        
    # Return the resulting roman numeral string in lowercase
    return roman_numeral.lower()
