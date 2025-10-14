def closest_integer(value):
    value = float(value)
    if value >= 0:
        if value - int(value) >= 0.5:
            return int(value) + 1
        else:
            return int(value)
    else:
        if abs(value) - abs(int(value)) >= 0.5:
            return int(value) - 1
        else:
            return int(value)
