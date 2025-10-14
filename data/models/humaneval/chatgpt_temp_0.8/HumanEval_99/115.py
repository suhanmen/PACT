import math

def closest_integer(value):
    num = float(value)
    if num >= 0:
        closest_int = math.floor(num + 0.5)
    else:
        closest_int = math.ceil(num - 0.5)
    return closest_int
