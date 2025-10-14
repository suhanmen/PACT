def closest_integer(value):
    value = float(value)
    integer_part = int(value)
    decimal_part = value - integer_part

    if decimal_part == 0.5:
        if integer_part % 2 == 0:
            return integer_part
        else:
            return integer_part + 1
    elif decimal_part > 0.5:
        return integer_part + 1
    else:
        return integer_part
