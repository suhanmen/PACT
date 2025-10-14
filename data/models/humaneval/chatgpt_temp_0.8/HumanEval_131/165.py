def digits(n):
    product = 1
    has_odd_digit = False
    for digit in str(n):
        digit = int(digit)
        if digit % 2 == 1:
            product *= digit
            has_odd_digit = True
    if has_odd_digit:
        return product
    else:
        return 0
