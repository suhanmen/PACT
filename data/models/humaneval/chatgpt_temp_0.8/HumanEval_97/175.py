def multiply(a, b):
    unit_a = abs(a) % 10
    unit_b = abs(b) % 10
    if unit_a == 0 or unit_b == 0:
        return 0
    if a < 0:
        unit_a *= -1
    if b < 0:
        unit_b *= -1
    return unit_a * unit_b
