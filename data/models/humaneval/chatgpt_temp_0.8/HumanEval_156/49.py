def int_to_mini_roman(number):
    if not 1 <= number <= 1000:
        raise ValueError('Number out of range')
    
    # Define the mappings between arabic and roman numerals
    roman_mappings = [
        (1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'),
        (100, 'c'), (90, 'xc'), (50, 'l'), (40, 'xl'),
        (10, 'x'), (9, 'ix'), (5, 'v'), (4, 'iv'), (1, 'i')
    ]
    
    # Convert the number to roman numeral form
    roman_numeral = ''
    for arabic, roman in roman_mappings:
        while number >= arabic:
            roman_numeral += roman
            number -= arabic
    
    # Convert the roman numeral to lowercase and return it
    return roman_numeral.lower()
