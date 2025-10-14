def closest_integer(value):
    num = float(value)
    if num > 0:
        integer_part = int(num)
        if num - integer_part >= 0.5:
            return integer_part + 1
        else:
            return integer_part
    elif num < 0:
        integer_part = int(num)
        if num - integer_part <= -0.5:
            return integer_part - 1
        else:
            return integer_part
    else:
        return 0
