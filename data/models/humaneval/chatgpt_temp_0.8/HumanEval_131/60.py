def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    prod = 1
    even = True
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            even = False
            prod *= digit
        n //= 10
    return prod if not even else 0
