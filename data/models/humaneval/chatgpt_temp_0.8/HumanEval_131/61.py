def digits(n):
    odd_product = 1
    even_digits = True
    while n > 0:
        digit = n % 10
        if digit % 2 == 1:
            odd_product *= digit
            even_digits = False
        n //= 10
    if even_digits:
        return 0
    else:
        return odd_product
