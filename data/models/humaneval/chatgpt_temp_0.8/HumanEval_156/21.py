def int_to_mini_roman(number):
    # Define the mapping from integers to Roman numerals
    roman_numerals = {
        1000: 'm', 900: 'cm', 500: 'd', 400: 'cd',
        100: 'c', 90: 'xc', 50: 'l', 40: 'xl',
        10: 'x', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'
    }
    # Check if the input number is valid
    if not isinstance(number, int) or not 1 <= number <= 1000:
        raise ValueError("Input must be an integer between 1 and 1000")
    # Convert the number to Roman numerals
    result = ""
    for value, numeral in roman_numerals.items():
        while number >= value:
            result += numeral
            number -= value
    # Return the result in lowercase
    return result.lower()
