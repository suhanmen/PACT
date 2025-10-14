python
def int_to_mini_roman(number):
    # Define a dictionary mapping integer values to roman numerals
    roman_numerals = {
        1: 'i', 4: 'iv', 5: 'v', 9: 'ix',
        10: 'x', 40: 'xl', 50: 'l', 90: 'xc',
        100: 'c', 400: 'cd', 500: 'd', 900: 'cm',
        1000: 'm'
    }
    # Define a list of integer values in descending order
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    
    # Edge case: number is outside the allowed range
    if not 1 <= number <= 1000:
        raise ValueError("Number must be between 1 and 1000.")
    
    # Convert the number to a roman numeral string
    result = ""
    for value in values:
        while number >= value:
            result += roman_numerals[value]
            number -= value
            
    # Return the lowercase roman numeral string
    return result.lower()
