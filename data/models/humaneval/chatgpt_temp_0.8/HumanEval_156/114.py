def int_to_mini_roman(number):
    # Define the roman numeral mappings
    roman_numerals = {
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

    # Define a list to store the roman numerals
    result = []

    # Iterate over the roman numeral mappings
    for value, numeral in roman_numerals.items():
        # Divide the number by the current value and truncate the result to get the number of times to repeat the numeral
        count = int(number / value)

        # Append the numeral to the result list count times
        result.append(numeral * count)

        # Subtract the value times the count from the number to get the remainder
        number -= value * count

    # Join the result list into a single string and return it in lowercase
    return ''.join(result).lower()
