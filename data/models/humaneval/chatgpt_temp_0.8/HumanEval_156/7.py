def int_to_mini_roman(number):
    # Map roman numeral symbols to their corresponding integer values
    roman_numerals = {'m': 1000, 'cm': 900, 'd': 500, 'cd': 400, 'c': 100, 'xc': 90, 
                      'l': 50, 'xl': 40, 'x': 10, 'ix': 9, 'v': 5, 'iv': 4, 'i': 1}
    
    # Check that the input number is within the allowed range
    if number < 1 or number > 1000:
        raise ValueError('Number must be between 1 and 1000')
    
    # Convert the number to a roman numeral string
    roman_numeral = ''
    for symbol, value in roman_numerals.items():
        while number >= value:
            roman_numeral += symbol
            number -= value
    
    # Convert the roman numeral string to lowercase and return it
    return roman_numeral.lower()
