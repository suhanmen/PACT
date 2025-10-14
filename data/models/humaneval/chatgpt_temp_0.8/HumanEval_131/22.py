def digits(n):
    odd_product = 1
    all_even = True
    for digit in str(n):
        if int(digit) % 2 == 0:
            continue
        odd_product *= int(digit)
        all_even = False
    if all_even:
        return 0
    else:
        return odd_product
