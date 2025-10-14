def digits(n):
    odd_product = 1
    all_even = True
    for digit in str(n):
        d = int(digit)
        if d % 2 != 0:
            odd_product *= d
            all_even = False
    if all_even:
        return 0
    else:
        return odd_product
