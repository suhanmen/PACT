def closest_integer(value):
    value = float(value)
    if value < 0:
        closest_int = int(value - 0.5)
    else:
        closest_int = int(value + 0.5)
    return closest_int
