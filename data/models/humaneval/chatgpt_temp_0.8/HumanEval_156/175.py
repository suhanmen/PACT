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
    # Define the mapping of roman numeral symbols and their values
    roman_mapping = {1000: 'm', 900: 'cm', 500: 'd', 400: 'cd', 100: 'c', 
                     90: 'xc', 50: 'l', 40: 'xl', 10: 'x', 9: 'ix', 
                     5: 'v', 4: 'iv', 1: 'i'}
    
    # Validate the input number
    if not isinstance(number, int) or number < 1 or number > 1000:
        raise ValueError('Number must be an integer between 1 and 1000.')
    
    # Convert the number to its roman numeral equivalent
    result = ''
    for value, symbol in roman_mapping.items():
        while number >= value:
            result += symbol
            number -= value
    
    # Return the lowercase roman numeral string
    return result.lower()
