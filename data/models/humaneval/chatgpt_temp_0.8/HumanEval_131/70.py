def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    even_count = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 1:
            product *= digit
        else:
            even_count += 1
        n //= 10
    if even_count == len(str(n)):
        return 0
    return product
