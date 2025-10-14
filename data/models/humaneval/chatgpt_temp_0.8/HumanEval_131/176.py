def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    odd_digits_product = 1
    all_digits_even = True
    for digit_char in str(n):
        digit = int(digit_char)
        if digit % 2 == 1:
            odd_digits_product *= digit
            all_digits_even = False
    if all_digits_even:
        return 0
    else:
        return odd_digits_product
