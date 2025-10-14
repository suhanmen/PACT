def closest_integer(value):
    value = float(value)
    integer = int(value)
    if value - integer >= 0.5:
        return integer + 1
    elif value - integer <= -0.5:
        return integer - 1
    else:
        return integer
