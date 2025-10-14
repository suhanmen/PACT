def digits(n):
    product = 1
    all_even = True
    while n > 0:
        digit = n % 10
        if digit % 2 == 1:
            product *= digit
            all_even = False
        n //= 10
    if all_even:
        return 0
    else:
        return product
