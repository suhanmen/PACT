def int_to_mini_roman(number):
    # Define the conversion table for roman numerals
    roman_numerals = {
        1000: 'm', 900: 'cm', 500: 'd', 400: 'cd',
        100: 'c', 90: 'xc', 50: 'l', 40: 'xl',
        10: 'x', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'
    }
    # Check input validity
    if 1 <= number <= 1000:
        # Initialize the result string
        result = ''
        # Iterate over the conversion table
        for value, symbol in roman_numerals.items():
            # Compute the number of times the current symbol fits into the input
            count = number // value
            # Add the symbol to the result string that many times
            result += symbol * count
            # Subtract the corresponding value from the input
            number -= value * count
        # Return the result string in lowercase
        return result.lower()
    else:
        # Raise an error if the input is out of range
        raise ValueError('Input must be between 1 and 1000')
