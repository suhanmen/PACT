def closest_integer(value):
    value = float(value)
    integer_part = int(value)
    if value - integer_part >= 0.5:
        return integer_part + 1
    elif value - integer_part <= -0.5:
        return integer_part - 1
    else:
        return integer_part
