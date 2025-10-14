def int_to_mini_roman(number):
    # Define the roman numeral equivalents of each digit in the ones, tens, hundreds, and thousands places
    thousands = ["", "m", "mm", "mmm"]
    hundreds = ["", "c", "cc", "ccc", "cd", "d", "dc", "dcc", "dccc", "cm"]
    tens = ["", "x", "xx", "xxx", "xl", "l", "lx", "lxx", "lxxx", "xc"]
    ones = ["", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix"]

    # Split the number into its individual digits
    thousands_digit = number // 1000
    hundreds_digit = (number % 1000) // 100
    tens_digit = (number % 100) // 10
    ones_digit = number % 10

    # Convert each digit to its roman numeral equivalent
    roman_numeral = thousands[thousands_digit] + hundreds[hundreds_digit] + tens[tens_digit] + ones[ones_digit]

    # Return the roman numeral in lowercase
    return roman_numeral.lower()
