def closest_integer(value):
    num = float(value)
    if num < 0:
        integer = int(num - 0.5)
    else:
        integer = int(num + 0.5)
    return integer
