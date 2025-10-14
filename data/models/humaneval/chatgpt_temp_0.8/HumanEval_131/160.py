def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    odd_prod = 1
    even_count = 0
    for digit in str(n):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_prod *= int(digit)
    if even_count == len(str(n)):
        return 0
    else:
        return odd_prod
