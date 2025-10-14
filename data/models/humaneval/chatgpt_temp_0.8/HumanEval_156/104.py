def int_to_mini_roman(number):
    # Define the mapping between integers and roman numerals
    roman_map = {
        1000: 'm', 900: 'cm', 500: 'd', 400: 'cd',
        100: 'c', 90: 'xc', 50: 'l', 40: 'xl',
        10: 'x', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'
    }
    # Check the input is within range
    if not 1 <= number <= 1000:
        raise ValueError('Number must be between 1 and 1000')
    # Convert the number to roman numerals
    result = ''
    for value, symbol in roman_map.items():
        while number >= value:
            result += symbol
            number -= value
    # Return the lowercase representation of the roman numerals
    return result.lower()
