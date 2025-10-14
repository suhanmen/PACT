def digits(n):
    odd_product = 1
    even_present = False
    while n != 0:
        digit = n % 10
        if digit % 2 != 0:
            odd_product *= digit
        else:
            even_present = True
        n //= 10
    if even_present:
        return odd_product
    else:
        return 0
