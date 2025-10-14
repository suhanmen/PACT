def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    odd_product = 1
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            odd_product *= digit
        n //= 10
    if odd_product == 1:
        return 0
    else:
        return odd_product
