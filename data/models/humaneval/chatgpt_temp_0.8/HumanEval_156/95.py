def int_to_mini_roman(number):
    # Define the roman numeral symbols and their corresponding values
    roman_symbols = {
        1000: 'm', 900: 'cm', 500: 'd', 400: 'cd', 100: 'c',
        90: 'xc', 50: 'l', 40: 'xl', 10: 'x', 9: 'ix',
        5: 'v', 4: 'iv', 1: 'i'
    }

    # Check if the input number is within the allowed range
    if number < 1 or number > 1000:
        raise ValueError("Input number must be between 1 and 1000")

    # Convert the number into roman numerals using the symbols and values
    roman_numeral = ""
    for value, symbol in roman_symbols.items():
        while number >= value:
            roman_numeral += symbol
            number -= value

    # Return the lowercase roman numeral string
    return roman_numeral.lower()
