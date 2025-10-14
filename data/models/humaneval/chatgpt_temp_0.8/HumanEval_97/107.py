def multiply(a, b):
    last_digit_a = abs(a) % 10
    last_digit_b = abs(b) % 10
    if last_digit_a == 0 or last_digit_b == 0:
        return 0
    else:
        product = last_digit_a * last_digit_b
        return product
