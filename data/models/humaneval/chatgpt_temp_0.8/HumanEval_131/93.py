def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    has_even_digit = False
    for digit in str(n):
        if int(digit) % 2 != 0:
            product *= int(digit)
        else:
            has_even_digit = True
    return 0 if not product or has_even_digit else product
