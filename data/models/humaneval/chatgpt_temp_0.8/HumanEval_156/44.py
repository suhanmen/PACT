def int_to_mini_roman(number):
    # Define the mapping of roman numerals to integers
    roman_map = {
        1000: 'm',
        900: 'cm',
        500: 'd',
        400: 'cd',
        100: 'c',
        90: 'xc',
        50: 'l',
        40: 'xl',
        10: 'x',
        9: 'ix',
        5: 'v',
        4: 'iv',
        1: 'i'
    }

    # Make sure the input number is valid
    if not 1 <= number <= 1000:
        raise ValueError("Number must be between 1 and 1000")

    # Convert the number to a roman numeral string
    result = ''
    for value, numeral in roman_map.items():
        while number >= value:
            result += numeral
            number -= value

    # Return the result in lowercase
    return result.lower()
