def int_to_mini_roman(number):
    roman = {
        1000: 'm', 900: 'cm', 500: 'd', 400: 'cd',
        100: 'c', 90: 'xc', 50: 'l', 40: 'xl',
        10: 'x', 9: 'ix', 5: 'v', 4: 'iv',
        1: 'i'
    }
    if number < 1 or number > 1000:
        raise ValueError('Number out of range')
    result = ''
    for value, letter in roman.items():
        while number >= value:
            result += letter
            number -= value
    return result.lower()
