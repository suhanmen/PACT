def closest_integer(value):
    num = float(value)
    if num >= 0:
        integer_part = int(num + 0.5)
    else:
        integer_part = int(num - 0.5)
    return integer_part
