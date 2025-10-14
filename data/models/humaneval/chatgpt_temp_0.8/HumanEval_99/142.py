def closest_integer(value):
    number = float(value)
    integer_part = int(number)
    decimal_part = number - integer_part

    if decimal_part < 0.5:
        return integer_part
    elif decimal_part > 0.5:
        return integer_part + 1
    else:
        if integer_part < 0:
            return integer_part - 1
        else:
            return integer_part + 1
