def digits(n):
    odd_digits_product = 1
    has_odd_digit = False
    while n > 0:
        digit = n % 10
        if digit % 2 == 1:
            odd_digits_product *= digit
            has_odd_digit = True
        n = n // 10
    return odd_digits_product if has_odd_digit else 0
