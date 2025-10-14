def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """
    # Define the mapping of Roman numerals to integers
    roman_numerals = {
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
    # Initialize an empty string to store the Roman numeral
    roman = ""
    # Iterate over the Roman numeral mapping
    for value, letter in roman_numerals.items():
        # Determine how many times the current value can be subtracted from the input
        count = number // value
        # Append the current letter to the Roman numeral string count number of times
        roman += letter * count
        # Subtract the current value times the count from the input number
        number -= value * count
    # Return the lowercase Roman numeral string
    return roman.lower()
