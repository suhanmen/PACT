def closest_integer(value):
    value = float(value)
    if value >= 0:
        # Round to nearest integer
        if value % 1 < 0.5:
            return int(value)
        else:
            return int(value) + 1
    else:
        # Round to nearest integer
        if abs(value) % 1 < 0.5:
            return int(value)
        else:
            return int(value) - 1
