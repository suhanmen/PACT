def closest_integer(value):
    value = float(value)
    if value < 0:
        integer_value = int(value - 0.5)
    else:
        integer_value = int(value + 0.5)
    return integer_value
