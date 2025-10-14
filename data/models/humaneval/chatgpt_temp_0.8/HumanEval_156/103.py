def int_to_mini_roman(number):
    roman_numerals = { 
        1: "i", 
        4: "iv", 
        5: "v", 
        9: "ix", 
        10: "x", 
        40: "xl", 
        50: "l", 
        90: "xc", 
        100: "c", 
        400: "cd", 
        500: "d", 
        900: "cm", 
        1000: "m"
    }
    
    if number < 1 or number > 1000:
        raise ValueError("Number must be between 1 and 1000")
    
    result = ""
    for value, numeral in sorted(roman_numerals.items(), reverse=True):
        while number >= value:
            result += numeral
            number -= value
            
    return result.lower()
