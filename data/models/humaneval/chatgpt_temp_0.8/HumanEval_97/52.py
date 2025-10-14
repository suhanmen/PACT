def multiply(a, b):
    a_unit = abs(a) % 10
    b_unit = abs(b) % 10
    if a_unit == 0 or b_unit == 0:
        return 0
    product = a_unit * b_unit
    return product if a * b > 0 else -product
