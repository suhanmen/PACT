def digits(n):
    odd_product = 1
    all_even = True
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            odd_product *= digit
            all_even = False
        n //= 10
    if all_even:
        return 0
    else:
        return odd_product
