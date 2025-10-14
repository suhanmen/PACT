def closest_integer(value):
    # Convert the value to a float
    value = float(value)

    # If the value is already an integer, return it
    if value.is_integer():
        return int(value)

    # Otherwise, find the two integers closest to the value
    lower_int = int(value)
    upper_int = lower_int + 1

    # Calculate the distances from the value to each integer
    lower_dist = value - lower_int
    upper_dist = upper_int - value

    # If the distances are equal, round away from zero
    if lower_dist == upper_dist:
        return int(upper_int if value > 0 else lower_int)

    # Otherwise, return the closest integer
    return int(upper_int if upper_dist < lower_dist else lower_int)
