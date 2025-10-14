def multiply(a, b):
    last_a = abs(a) % 10
    last_b = abs(b) % 10
    if last_a == 0 or last_b == 0:
        return 0
    product = last_a * last_b
    if a < 0 and b < 0:
        return product
    elif a < 0 or b < 0:
        return -product
    else:
        return product
