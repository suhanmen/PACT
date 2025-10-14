def closest_integer(value):
    import math
    value = float(value)
    if value >= 0:
        integer_part = math.floor(value)
        if value - integer_part >= 0.5:
            return int(math.ceil(value))
        else:
            return int(integer_part)
    else:
        integer_part = math.ceil(value)
        if abs(value - integer_part) >= 0.5:
            return int(math.floor(value))
        else:
            return int(integer_part)
