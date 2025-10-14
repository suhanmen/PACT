def int_to_mini_roman(number):
    if not 1 <= number <= 1000:
        raise ValueError("Number must be between 1 and 1000")
    
    # Define the mapping of roman numerals to integers
    roman_map = {
        1000: 'm', 900: 'cm', 500: 'd', 400: 'cd',
        100: 'c', 90: 'xc', 50: 'l', 40: 'xl',
        10: 'x', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'
    }
    
    roman_numeral = ''
    for numeral, letter in roman_map.items():
        while number >= numeral:
            roman_numeral += letter
            number -= numeral
    
    return roman_numeral.lower()
