def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    odd_digits = [int(digit) for digit in str(n) if int(digit)%2 != 0]
    if len(odd_digits) == 0:
        return 0
    else:
        product = 1
        for digit in odd_digits:
            product *= digit
        return product
