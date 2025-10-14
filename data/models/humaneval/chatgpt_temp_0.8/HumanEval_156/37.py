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
    if not 1 <= number <= 1000:
        raise ValueError("number must be between 1 and 1000 (inclusive)")

    # Create a dictionary to map integers to their corresponding roman numerals
    roman_map = {
        1: 'i', 4: 'iv', 5: 'v', 9: 'ix',
        10: 'x', 40: 'xl', 50: 'l', 90: 'xc',
        100: 'c', 400: 'cd', 500: 'd', 900: 'cm',
        1000: 'm'
    }

    # Create a list of tuples containing the integer and its corresponding roman numeral
    roman_list = [(k, v) for k, v in roman_map.items()]

    # Sort the list in descending order of integer values
    roman_list.sort(reverse=True)

    # Convert the integer to its roman numeral equivalent
    result = ""
    for integer, numeral in roman_list:
        while number >= integer:
            result += numeral
            number -= integer

    return result.lower()
