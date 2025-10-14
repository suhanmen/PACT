def closest_integer(value):
    num = float(value)  # convert string to float
    if num >= 0:
        return int(num + 0.5)  # round up if decimal is >= 0.5
    else:
        return int(num - 0.5)  # round down if decimal is < 0.5
