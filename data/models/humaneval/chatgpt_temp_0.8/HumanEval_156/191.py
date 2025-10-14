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
        raise ValueError("Number must be between 1 and 1000")

    roman = ""
    digits = [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
              ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
              ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]

    for letter, value in digits:
        while number >= value:
            roman += letter
            number -= value

    return roman.lower()
