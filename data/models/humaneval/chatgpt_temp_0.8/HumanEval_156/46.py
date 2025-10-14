def int_to_mini_roman(number):
    # Define the roman numeral symbols and their values
    roman_symbols = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
        'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
        'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
    }
    # Check that the input is a valid integer within the allowed range
    if not isinstance(number, int) or not 1 <= number <= 1000:
        raise ValueError("Input must be a positive integer between 1 and 1000")
    # Convert the integer to its roman numeral representation
    result = ''
    for symbol, value in roman_symbols.items():
        while number >= value:
            result += symbol
            number -= value
    # Return the lowercase roman numeral string
    return result.lower()
