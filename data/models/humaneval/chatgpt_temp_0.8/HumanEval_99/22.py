def closest_integer(value):
    # Convert the input value to a float
    value = float(value)

    # Check if the value is already an integer
    if value.is_integer():
        return int(value)

    # Calculate the distance to the two closest integers
    lower_int = int(value)
    upper_int = lower_int + 1
    dist_lower = abs(value - lower_int)
    dist_upper = abs(value - upper_int)

    # If the distance to the lower integer is closer or equal to the upper one,
    # round down to the lower integer. Otherwise, round up to the upper integer.
    if dist_lower <= dist_upper:
        return lower_int
    else:
        return upper_int
