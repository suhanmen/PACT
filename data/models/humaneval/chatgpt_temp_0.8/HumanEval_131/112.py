def digits(n):
    odd_product = 1
    even_count = 0
    while n > 0:
        digit = n % 10
        if digit % 2 == 1:
            odd_product *= digit
        else:
            even_count += 1
        n //= 10
    if even_count == len(str(n)):
        return 0
    return odd_product
