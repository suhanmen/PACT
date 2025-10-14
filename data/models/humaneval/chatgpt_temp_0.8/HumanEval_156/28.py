def int_to_mini_roman(number):
    # Define a dictionary to store the roman numeral equivalents for each digit
    roman_dict = {
        1: 'i',
        4: 'iv',
        5: 'v',
        9: 'ix',
        10: 'x',
        40: 'xl',
        50: 'l',
        90: 'xc',
        100: 'c',
        400: 'cd',
        500: 'd',
        900: 'cm',
        1000: 'm'
    }

    # Define a list to store the keys of the roman_dict in descending order
    keys = sorted(roman_dict.keys(), reverse=True)

    # Initialize variables to keep track of the remaining number and the resulting mini roman numeral string
    remaining_num = number
    mini_roman_numeral = ''

    # Loop through the keys of the roman_dict
    for key in keys:
        # Determine how many times the current key can be subtracted from the remaining number
        quotient, remainder = divmod(remaining_num, key)

        # Add the corresponding roman numeral to the mini_roman_numeral string for each time it can be subtracted
        mini_roman_numeral += roman_di
