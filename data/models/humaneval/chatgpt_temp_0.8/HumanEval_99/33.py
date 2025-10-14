def closest_integer(value):
    value = float(value)
    if value >= 0:
        int_val = int(value + 0.5)
        if value - int_val == 0.5:
            return int_val + 1
        else:
            return int_val
    else:
        int_val = int(value - 0.5)
        if int_val - value == 0.5:
            return int_val - 1
        else:
            return int_val
