def int_to_mini_roman(number):
    if number < 1 or number > 1000:
        raise ValueError("Number must be between 1 and 1000")
    
    # Define the mapping of roman numerals and their values
    roman_mapping = {
        1000: 'm', 900: 'cm', 500: 'd', 400: 'cd',
        100: 'c', 90: 'xc', 50: 'l', 40: 'xl',
        10: 'x', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'
    }

    roman_numeral = ''
    for value, numeral in roman_mapping.items():
        while number >= value:
            roman_numeral += numeral
            number -= value

    return roman_numeral.lower()
