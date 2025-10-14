def closest_integer(value):
    number = float(value)
    if number > 0:
        integer = int(number + 0.5)
    else:
        integer = int(number - 0.5)
    return integer
