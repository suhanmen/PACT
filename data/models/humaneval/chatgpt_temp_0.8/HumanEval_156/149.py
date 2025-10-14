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
    # Define the mapping of roman numerals and their values
    roman_values = [('m', 1000), ('cm', 900), ('d', 500), ('cd', 400),
                    ('c', 100), ('xc', 90), ('l', 50), ('xl', 40),
                    ('x', 10), ('ix', 9), ('v', 5), ('iv', 4), ('i', 1)]
    
    # Check that the input is within the allowed range
    if number < 1 or number > 1000:
        raise ValueError('Number out of range')
    
    # Build the roman numeral string by iterating through the mapping
    roman_numeral = ''
    for roman, value in roman_values:
        while number >= value:
            roman_numeral += roman
            number -= value
    
    # Return the roman numeral in lowercase
    return roman_numeral.lower()
