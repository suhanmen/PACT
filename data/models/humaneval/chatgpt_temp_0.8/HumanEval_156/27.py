def int_to_mini_roman(number):
    # Define the mapping between numbers and Roman numeral symbols
    roman_map = {1000: 'm', 900: 'cm', 500: 'd', 400: 'cd', 100: 'c', 90: 'xc',
                 50: 'l', 40: 'xl', 10: 'x', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'}

    # Check that the input number is valid
    if not 1 <= number <= 1000:
        raise ValueError('Input number must be between 1 and 1000')

    # Convert the number to its Roman numeral representation
    result = ''
    for value, symbol in roman_map.items():
        while number >= value:
            result += symbol
            number -= value

    # Return the lowercase Roman numeral string
    return result.lower()
