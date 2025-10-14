def digits(n):
    odd_product = 1
    has_odd_digit = False
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            odd_product *= digit
            has_odd_digit = True
        n //= 10
    if has_odd_digit:
        return odd_product
    else:
        return 0
