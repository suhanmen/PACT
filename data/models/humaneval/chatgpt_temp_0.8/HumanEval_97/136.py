def multiply(a, b):
    digit_a = abs(a) % 10
    digit_b = abs(b) % 10
    if digit_a == 0 or digit_b == 0:
        return 0
    else:
        product = digit_a * digit_b
        return product if a * b > 0 else -product
