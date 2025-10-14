def digits(n):
    """
    Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    """
    product = 1
    all_even = True
    for digit in str(n):
        if int(digit) % 2 != 0:
            product *= int(digit)
            all_even = False
    if all_even:
        return 0
    else:
        return product
