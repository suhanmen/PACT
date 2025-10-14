def digits(n):
    odd_product = 1
    has_even_digit = False
    for digit in str(n):
        if int(digit) % 2 == 0:
            has_even_digit = True
        else:
            odd_product *= int(digit)
    return odd_product if has_even_digit else 0
