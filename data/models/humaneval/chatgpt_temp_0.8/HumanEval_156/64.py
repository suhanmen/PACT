def int_to_mini_roman(number):
    # Map roman numeral symbols to their integer values
    roman_map = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1,
    }
    # Check that the number is within the allowed range
    if number < 1 or number > 1000:
        raise ValueError('Number must be between 1 and 1000')
    # Convert the number to a roman numeral string
    roman_numeral = ''
    for symbol, value in roman_map.items():
        while number >= value:
            roman_numeral += symbol
            number -= value
    # Return the roman numeral string in lowercase
    return roman_numeral.lower()
