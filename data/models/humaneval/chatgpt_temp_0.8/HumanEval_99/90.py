def closest_integer(value):
    value = float(value)
    rounded_value = round(value)
    if rounded_value > value:
        return int(rounded_value - 1)
    else:
        return int(rounded_value)
