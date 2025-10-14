def int_to_mini_roman(number):
    # Define the mapping between integers and roman numerals
    roman_map = {
        1000: 'm', 900: 'cm', 500: 'd', 400: 'cd',
        100: 'c', 90: 'xc', 50: 'l', 40: 'xl',
        10: 'x', 9: 'ix', 5: 'v', 4: 'iv', 1: 'i'
    }
    # Check that the input is within the allowed range
    if not 1 <= number <= 1000:
        raise ValueError("Input must be between 1 and 1000")
    # Initialize the result string
    result = ""
    # Iterate over the roman_map and build the result string
    for integer, numeral in roman_map.items():
        while number >= integer:
            result += numeral
            number -= integer
    # Return the result string in lowercase
    return result.lower()
