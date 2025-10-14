def closest_integer(value):
    value = float(value)
    if value >= 0:
        if value - int(value) < 0.5:
            return int(value)
        else:
            return int(value) + 1
    else:
        if abs(value - int(value)) < 0.5:
            return int(value)
        else:
            return int(value) - 1
