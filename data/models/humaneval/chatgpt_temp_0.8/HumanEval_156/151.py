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
    # Define lookup tables for roman numerals
    digits = ['','i','ii','iii','iv','v','vi','vii','viii','ix']
    tens = ['','x','xx','xxx','xl','l','lx','lxx','lxxx','xc']
    hundreds = ['','c','cc','ccc','cd','d','dc','dcc','dccc','cm']
    thousands = ['','m','mm','mmm']

    # Split number into thousands, hundreds, tens, and ones places
    thousands_place = thousands[number // 1000]
    hundreds_place = hundreds[number // 100 % 10]
    tens_place = tens[number // 10 % 10]
    ones_place = digits[number % 10]

    # Combine the roman numerals and return as lowercase string
    return (thousands_place + hundreds_place + tens_place + ones_place).lower()
