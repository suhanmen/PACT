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
    # Define the possible roman numeral values and their corresponding integer values
    roman_numerals = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100,
                      'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}

    # Convert the number to a roman numeral
    roman_numeral = ''
    for numeral, value in roman_numerals.items():
        while number >= value:
            roman_numeral += numeral
            number -= value

    # Return the roman numeral in lowercase
    return roman_numeral.lower()
