def multiply(a, b):
    last_digit_a = abs(a) % 10
    last_digit_b = abs(b) % 10
    return last_digit_a * last_digit_b
