def int_to_mini_roman(number):
    # Define a dictionary that maps values to their Roman numeral equivalents
    roman_dict = {1000: 'm', 900: 'cm', 500: 'd', 400: 'cd', 100: 'c', 90: 'xc', 50: 'l', 40: 'xl', 10: 'x', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'}
    
    # Ensure that the input is within the allowed range
    if number < 1 or number > 1000:
        raise ValueError("Input must be between 1 and 1000")
    
    # Initialize an empty string to hold the result
    result = ''
    
    # Iterate through the dictionary keys in descending order
    for value in sorted(roman_dict.keys(), reverse=True):
        # Add the Roman numeral equivalent to the result as many times as possible
        while number >= value:
            result += roman_dict[value]
            number -= value
    
    # Return the result in lowercase
    return result.lower()
