def digits(n):
    odd_digits_product = 1
    even_digits_exist = False
    while n > 0:
        digit = n % 10
        if digit % 2 == 1:
            odd_digits_product *= digit
        else:
            even_digits_exist = True
        n //= 10
    return odd_digits_product if even_digits_exist else 0
