def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    odd_product = 1
    even_flag = True

    for digit in str(n):
        if int(digit) % 2 == 0:
            even_flag = True
        else:
            odd_product *= int(digit)
            even_flag = False

    return odd_product if not even_flag else 0
