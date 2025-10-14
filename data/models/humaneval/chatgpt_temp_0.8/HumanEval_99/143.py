def closest_integer(value):
    # Convert the input value to a float
    value_float = float(value)

    # Get the floor and ceiling of the value
    floor_value = int(value_float - 0.5)
    ceil_value = int(value_float + 0.5)

    # Check which integer is closest to the value
    if abs(floor_value - value_float) < abs(ceil_value - value_float):
        return floor_value
    elif abs(ceil_value - value_float) < abs(floor_value - value_float):
        return ceil_value
    else:
        # If the value is equidistant from two integers, round it away from zero
        if value_float < 0:
            return ceil_value
        else:
            return floor_value
