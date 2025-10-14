def digits(n):
    product = 1
    even_digit = False
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            product *= digit
        else:
            even_digit = True
        n //= 10
    if even_digit:
        return product
    else:
        return 0
