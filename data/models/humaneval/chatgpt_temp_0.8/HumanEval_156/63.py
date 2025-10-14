def int_to_mini_roman(number):
    # Define the roman numeral symbols and their values
    roman_numerals = {
        1000: 'm', 900: 'cm', 500: 'd', 400: 'cd',
        100: 'c', 90: 'xc', 50: 'l', 40: 'xl',
        10: 'x', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'
    }
    
    # Check if the number is within the allowed range
    if number < 1 or number > 1000:
        raise ValueError('Number must be between 1 and 1000')

    # Convert the number to a roman numeral string
    roman_numeral = ''
    for value, symbol in roman_numerals.items():
        while number >= value:
            roman_numeral += symbol
            number -= value

    # Return the roman numeral in lowercase
    return roman_numeral.lower()
