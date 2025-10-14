def digits(n):
    odd_product = 1
    even_flag = False
    for digit in str(n):
        if int(digit) % 2 == 0:
            even_flag = True
        else:
            odd_product *= int(digit)
    if even_flag:
        return 0
    else:
        return odd_product
