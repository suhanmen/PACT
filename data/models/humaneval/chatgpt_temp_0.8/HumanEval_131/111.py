def digits(n):
    """
    Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    """
    product = 1
    has_odd = False
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
            has_odd = True
    return product if has_odd else 0
