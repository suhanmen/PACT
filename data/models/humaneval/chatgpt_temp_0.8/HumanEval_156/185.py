def int_to_mini_roman(number):
    roman_map = [(1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'), (100, 'c'), 
                (90, 'xc'), (50, 'l'), (40, 'xl'), (10, 'x'), (9, 'ix'), (5, 'v'), 
                (4, 'iv'), (1, 'i')]
    if not 0 < number <= 1000:
        return "Invalid input"
    roman_str = ""
    for value, symbol in roman_map:
        while number >= value:
            roman_str += symbol
            number -= value
    return roman_str.lower()
