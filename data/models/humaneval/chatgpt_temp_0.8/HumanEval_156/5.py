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
    # Define the mapping of integers to roman numerals
    roman_mapping = {
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
    
    # Check if the number is within the valid range
    if number < 1 or number > 1000:
        raise ValueError("Number must be between 1 and 1000 inclusive")
    
    # Convert the number to its roman numeral equivalent
    roman_numeral = ''
    for integer, numeral in roman_mapping.items():
        while number >= integer:
            roman_numeral += numeral
            number -= integer
    
    # Return the roman numeral in lowercase
    return roman_numeral.lower()
