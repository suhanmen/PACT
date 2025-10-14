def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
    if product == 1:
        return 0
    else:
        return product
