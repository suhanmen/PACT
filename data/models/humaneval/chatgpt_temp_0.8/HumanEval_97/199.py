def multiply(a, b):
    last_digit_a = abs(a) % 10
    last_digit_b = abs(b) % 10
    if a == 0 or b == 0:
        return 0
    elif a < 0 and b > 0:
        return -last_digit_a * last_digit_b
    elif a > 0 and b < 0:
        return last_digit_a * -last_digit_b
    else:
        return last_digit_a * last_digit_b
