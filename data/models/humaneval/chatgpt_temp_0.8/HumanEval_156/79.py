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

    # Define the Roman numerals and their values
    roman_numerals = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
        'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
        'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
    }

    # Check for valid input
    if not isinstance(number, int) or number < 1 or number > 1000:
        raise ValueError('Input must be a positive integer between 1 and 1000.')

    # Convert the number to Roman numerals using a greedy algorithm
    result = ''
    for symbol, value in roman_numerals.items():
        while number >= value:
            result += symbol
            number -= value

    # Return the lowercase Roman numeral string
    return result.lower()
