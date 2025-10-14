def int_to_mini_roman(number):
    if not isinstance(number, int) or number < 1 or number > 1000:
        raise ValueError("Input must be an integer between 1 and 1000.")
    
    roman_numerals = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
        'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
        'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
    }
    
    result = ''
    
    for numeral, value in roman_numerals.items():
        while number >= value:
            result += numeral
            number -= value
    
    return result.lower()
