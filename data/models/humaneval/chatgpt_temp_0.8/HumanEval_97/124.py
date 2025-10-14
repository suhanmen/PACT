def multiply(a, b):
    a_last_digit = abs(a) % 10
    b_last_digit = abs(b) % 10
    if a_last_digit == 0 or b_last_digit == 0:
        return 0
    if a < 0:
        a_last_digit *= -1
    if b < 0:
        b_last_digit *= -1
    return a_last_digit * b_last_digit
