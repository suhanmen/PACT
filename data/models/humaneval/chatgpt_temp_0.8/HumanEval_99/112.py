def closest_integer(value):
    # Convert the input value to a float
    x = float(value)

    # Check if the value is already an integer
    if x.is_integer():
        return int(x)

    # Calculate the two integers that the value is between
    lower_int = int(x)
    upper_int = lower_int + 1

    # Calculate the distances from the value to each integer
    lower_dist = abs(x - lower_int)
    upper_dist = abs(x - upper_int)

    # Determine which integer is closest and return it
    if lower_dist < upper_dist:
        return lower_int
    elif upper_dist < lower_dist:
        return upper_int
    else:
        # If the distances are equal, round away from zero
        if x > 0:
            return upper_int
        else:
            return lower_int
