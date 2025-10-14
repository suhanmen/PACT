def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    contains_odd = False
    while n > 0:
        digit = n % 10
        if digit % 2 == 1:
            contains_odd = True
            product *= digit
        n //= 10
    if contains_odd:
        return product
    else:
        return 0
