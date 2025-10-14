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
    # Define mapping of roman numerals to integers
    roman_numerals = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100,
                      'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    
    # Check if number is within range
    if number < 1 or number > 1000:
        return None
    
    # Initialize empty string to store roman numeral
    roman_numeral = ''
    
    # Iterate through mapping of roman numerals to integers
    for numeral, value in roman_numerals.items():
        # Calculate the number of times the current value goes into the number
        quotient = number // value
        # Add the current roman numeral to the string that many times
        roman_numeral += quotient * numeral
        # Update the number with the remainder
        number %= value
    # Return the roman numeral in lowercase
    return roman_numeral.lower()
