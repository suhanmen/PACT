python
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    prod = 1
    even_digit_count = 0
    for digit in str(n):
        if int(digit) % 2 == 0:
            even_digit_count += 1
        else:
            prod *= int(digit)
    if even_digit_count == len(str(n)):
        return 0
    else:
        return prod
