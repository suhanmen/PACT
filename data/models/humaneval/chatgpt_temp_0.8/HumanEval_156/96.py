def int_to_mini_roman(number):
    # Define a dictionary that maps integer values to their Roman numeral equivalents
    roman_numerals = {
        1: 'i', 4: 'iv', 5: 'v', 9: 'ix', 10: 'x', 40: 'xl', 50: 'l', 90: 'xc',
        100: 'c', 400: 'cd', 500: 'd', 900: 'cm', 1000: 'm'
    }
    
    # Define a list of the integer values in descending order
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    
    # Initialize an empty string to build the final Roman numeral string
    roman_numeral = ""
    
    # Iterate over the integer values in descending order
    for value in values:
        # Compute the number of times the current value goes into the input number
        quotient, number = divmod(number, value)
        
        # Append the corresponding Roman numeral string to the final string
        roman_numeral += roman_numerals[value] * quotient
    
    # Return the final Roman numeral string in lowercase
    return roman_numeral.lower()
