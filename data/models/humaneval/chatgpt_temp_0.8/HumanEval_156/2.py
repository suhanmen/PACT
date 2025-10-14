# CANNOT PARSE CODE SNIPPET
def int_to_mini_roman(num):
    romans = {
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

    if num < 1 or num > 1000:
        raise ValueError("Number must be between 1 and 1000")

    result = ''
    for value, letter in romans.items():
        while num >= value:
            result += letter
            num -= value

    return result.lower()
