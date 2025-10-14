def int_to_mini_roman(number):
    if not 1 <= number <= 1000:
        raise ValueError("Invalid input, number must be between 1 and 1000")
    roman_numerals = {
        1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x',
        40: 'xl', 50: 'l', 90: 'xc', 100: 'c',
        400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'
    }
    result = ''
    for numeral, value in sorted(roman_numerals.items(), reverse=True):
        while number >= numeral:
            result += value
            number -= numeral
    return result.lower()
