def int_to_mini_roman(number):
    # Define a dictionary with roman numeral equivalents for numbers.
    roman_numeral_dict = {
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
    
    # Define a list of keys in the dictionary.
    roman_numeral_keys = sorted(roman_numeral_dict.keys(), reverse=True)
    
    # Ensure that the number is within the specified range.
    if number < 1 or number > 1000:
        raise ValueError("Number must be between 1 and 1000.")
    
    # Initialize an empty string to store the roman numeral equivalent.
    roman_numeral = ""
    
    # Convert the number to its roman numeral equivalent.
    for key in roman_numeral_keys:
        while number >= key:
            roman_numeral += roman_numeral_dict[key]
            number -= key
    
    # Return the roman numeral in lowercase.
    return roman_numera
