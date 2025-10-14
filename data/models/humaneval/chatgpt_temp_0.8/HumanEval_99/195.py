def closest_integer(value):
    value = float(value)
    abs_value = abs(value)
    integer_floor = int(value)
    integer_ceil = integer_floor + 1
    
    if abs_value - abs(integer_floor) < abs(integer_ceil) - abs_value:
        return integer_floor
    elif abs_value - abs(integer_floor) > abs(integer_ceil) - abs_value:
        return integer_ceil
    else:
        return integer_ceil if value > 0 else integer_floor
