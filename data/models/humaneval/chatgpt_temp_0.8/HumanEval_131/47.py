def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    all_digits_even = True
    for digit in str(n):
        if int(digit) % 2 != 0:
            product *= int(digit)
            all_digits_even = False
    if all_digits_even:
        return 0
    else:
        return product
