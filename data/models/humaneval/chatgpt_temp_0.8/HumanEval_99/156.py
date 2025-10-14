def closest_integer(value):
    value = float(value)
    if value >= 0:
        integer_part = int(value)
        if value - integer_part < 0.5:
            return integer_part
        else:
            return integer_part + 1
    else:
        integer_part = int(value)
        if integer_part - value < 0.5:
            return integer_part
        else:
            return integer_part - 1
