def digits(n):
    odd_digits_product = 1
    even_digits_count = 0
    for digit in str(n):
        if int(digit) % 2 == 0:
            even_digits_count += 1
        else:
            odd_digits_product *= int(digit)
    if even_digits_count == len(str(n)):
        return 0
    else:
        return odd_digits_product
