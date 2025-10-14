def digits(n):
    product = 1
    even_flag = True
    for digit in str(n):
        if int(digit) % 2 != 0:
            product *= int(digit)
            even_flag = False
    if even_flag:
        return 0
    return product
