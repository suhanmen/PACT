def closest_integer(value):
    float_val = float(value)
    if float_val < 0:
        integer_val = int(float_val - 0.5)
    else:
        integer_val = int(float_val + 0.5)
    return integer_val
