def closest_integer(value):
    value = float(value) # convert the input string to a float
    if value >= 0:
        return int(value + 0.5) # round up if the decimal is >= 0.5
    else:
        return int(value - 0.5) # round down if the decimal is < 0.5
