def closest_integer(value):
    # Convert the string value to a float
    value = float(value)

    # Get the floor and ceiling of the float value
    floor_value = int(value // 1)
    ceil_value = int(value // 1) + 1

    # Calculate the difference between the value and the floor and ceil
    diff_floor = abs(value - floor_value)
    diff_ceil = abs(value - ceil_value)

    # If the difference to the floor is less than or equal to the difference
    # to the ceiling, return the floor value. Otherwise, return the ceil value.
    if diff_floor <= diff_ceil:
        return floor_value
    else:
        return ceil_value
