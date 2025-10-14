def closest_integer(value):
    value = float(value)
    if value >= 0:
        integer = int(value + 0.5)
    else:
        integer = int(value - 0.5)
    return integer
