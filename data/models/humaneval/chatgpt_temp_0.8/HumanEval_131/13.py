def digits(n):
    product = 1
    all_even = True
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
            all_even = False
    if all_even:
        return 0
    else:
        return product
