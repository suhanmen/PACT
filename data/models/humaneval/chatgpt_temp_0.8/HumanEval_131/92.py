def digits(n):
    odd_digits_product = 1
    all_digits_even = True
    for digit in str(n):
        if int(digit) % 2 != 0:
            odd_digits_product *= int(digit)
            all_digits_even = False
    if all_digits_even:
        return 0
    else:
        return odd_digits_product
