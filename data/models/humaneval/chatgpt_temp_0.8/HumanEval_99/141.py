def closest_integer(value):
    value = float(value)
    if value < 0:
        value -= 0.5
    else:
        value += 0.5
    return int(value)
