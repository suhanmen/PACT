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
    if not 1 <= number <= 1000:
        raise ValueError("Number must be between 1 and 1000, inclusive")
    roman_numeral_mapping = (
        ("m", 1000), ("cm", 900), ("d", 500), ("cd", 400),
        ("c", 100), ("xc", 90), ("l", 50), ("xl", 40),
        ("x", 10), ("ix", 9), ("v", 5), ("iv", 4),
        ("i", 1)
    )
    result = ""
    for roman, num in roman_numeral_mapping:
        while number >= num:
            result += roman
            number -= num
    return result.lower()
