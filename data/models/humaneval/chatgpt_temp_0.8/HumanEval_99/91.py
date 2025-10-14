def closest_integer(value):
    # convert value to float
    value = float(value)

    # find the closest integer
    if value >= 0:
        closest = int(value + 0.5)
    else:
        closest = int(value - 0.5)

    return closest
