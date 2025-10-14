def int_to_mini_roman(number):
    roman_map = {
        1: 'i', 4: 'iv', 5: 'v', 9: 'ix',
        10: 'x', 40: 'xl', 50: 'l', 90: 'xc',
        100: 'c', 400: 'cd', 500: 'd', 900: 'cm',
        1000: 'm'
    }
    roman_num = ''
    for r in sorted(roman_map.keys(), reverse=True):
        while number >= r:
            roman_num += roman_map[r]
            number -= r
    return roman_num.lower()
