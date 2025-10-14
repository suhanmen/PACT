def int_to_mini_roman(number):
    if not 1 <= number <= 1000:
        raise ValueError("number must be between 1 and 1000, inclusive")
    # Define the mapping of decimal values to Roman numeral symbols
    roman_map = {1000: 'm', 900: 'cm', 500: 'd', 400: 'cd', 100: 'c',
                 90: 'xc', 50: 'l', 40: 'xl', 10: 'x', 9: 'ix',
                 5: 'v', 4: 'iv', 1: 'i'}
    # Initialize the result string
    result = ''
    # Iterate through the mapping, subtracting the largest possible value
    # and adding the corresponding symbol to the result string
    for value, symbol in roman_map.items():
        while number >= value:
            result += symbol
            number -= value
    # Return the result in lowercase
    return result.lower()
