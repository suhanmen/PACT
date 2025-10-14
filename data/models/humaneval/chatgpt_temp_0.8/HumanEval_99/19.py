def closest_integer(value):
    # Convert the given value to a float
    f_value = float(value)

    # Check if the value is already an integer
    if f_value.is_integer():
        return int(f_value)

    # Get the floor and ceiling values of the float
    floor_val = int(f_value // 1)
    ceil_val = int(f_value // 1 + 1)

    # Calculate the differences between the float and its floor/ceiling
    diff_floor = abs(f_value - floor_val)
    diff_ceil = abs(f_value - ceil_val)

    # Return the closer integer or the one farthest from zero in case of a tie
    if diff_floor < diff_ceil:
        return floor_val
    elif diff_ceil < diff_floor:
        return ceil_val
    else:
        return ceil_val if f_value > 0 else floor_val
