def int_to_mini_roman(number):
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

    if not 1 <= number <= 1000:
        raise ValueError("Invalid input. Number must be between 1 and 1000.")

    result = []
    for value, numeral in roman_numerals.items():
        while number >= value:
            result.append(numeral)
            number -= value

    return ''.join(result).lower()
