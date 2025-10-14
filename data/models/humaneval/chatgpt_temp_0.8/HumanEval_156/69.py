def int_to_mini_roman(number):
    # Define the conversion table for each digit
    roman_digits = ["", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix"]
    roman_tens = ["", "x", "xx", "xxx", "xl", "l", "lx", "lxx", "lxxx", "xc"]
    roman_hundreds = ["", "c", "cc", "ccc", "cd", "d", "dc", "dcc", "dccc", "cm"]
    roman_thousands = ["", "m"]

    # Get the individual digits of the number
    thousands = number // 1000
    hundreds = (number % 1000) // 100
    tens = (number % 100) // 10
    ones = number % 10

    # Convert each digit to its roman numeral equivalent
    roman = roman_thousands[thousands] + roman_hundreds[hundreds] + roman_tens[tens] + roman_digits[ones]

    return roman.lower()
