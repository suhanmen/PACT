def digits(n):
    product = 1
    even_flag = True
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            even_flag = False
            product *= digit
        n //= 10
    return product if not even_flag else 0
