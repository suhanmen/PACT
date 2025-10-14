def int_to_mini_roman(number):
    # Define a mapping of integer values to Roman numeral letters
    roman_map = {
        1000: "m",
        900: "cm",
        500: "d",
        400: "cd",
        100: "c",
        90: "xc",
        50: "l",
        40: "xl",
        10: "x",
        9: "ix",
        5: "v",
        4: "iv",
        1: "i"
    }
    
    # Make sure the input number is within the allowed range
    if number < 1 or number > 1000:
        raise ValueError("Number must be between 1 and 1000")
    
    # Initialize an empty string to accumulate the Roman numeral
    roman_numeral = ""
    
    # Loop through the mapping of integer values to Roman numerals
    for value, letter in roman_map.items():
        # Subtract the largest possible multiple of the current value from the input number
        while number >= value:
            roman_numeral += letter
            number -= value
    
    # Return the resulting Roman numeral in lowercase
    return roman_numeral.lower()
