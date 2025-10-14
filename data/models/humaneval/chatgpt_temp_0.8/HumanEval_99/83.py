def closest_integer(value):
    value = float(value)
    integer_part = int(value)
    decimal_part = abs(value - integer_part)
    if decimal_part < 0.5:
        return integer_part
    elif value > 0:
        return integer_part + 1
    else:
        return integer_part - 1
