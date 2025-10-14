def int_to_mini_roman(number):
    # Define a dictionary of roman numeral symbols and their corresponding values
    roman_symbols = {
        'm': 1000, 'cm': 900, 'd': 500, 'cd': 400,
        'c': 100, 'xc': 90, 'l': 50, 'xl': 40,
        'x': 10, 'ix': 9, 'v': 5, 'iv': 4,
        'i': 1
    }

    # Check if the number is within the allowed range
    if not 1 <= number <= 1000:
        raise ValueError("Number out of range")

    roman_numeral = ''
    # Loop through the roman symbols dictionary
    for symbol, value in roman_symbols.items():
        # Divide the number by the symbol value, keep the quotient and remainder
        quotient, number = divmod(number, value)
        # Add the roman symbol quotient times to the roman numeral string
        roman_numeral += symbol * quotient

    # Return the lowercase roman numeral string
    return roman_numeral.lower()
