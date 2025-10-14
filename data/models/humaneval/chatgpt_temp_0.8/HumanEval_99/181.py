def closest_integer(value):
    # Convert the input value to a float
    value = float(value)

    # Check if the value is already an integer
    if value.is_integer():
        return int(value)

    # Calculate the two closest integers to the value
    lower = int(value)
    upper = lower + 1

    # Calculate the distance to each integer
    dist_lower = value - lower
    dist_upper = upper - value

    # Check which integer is closer and return it
    if dist_lower < dist_upper:
        return lower
    elif dist_upper < dist_lower:
        return upper
    else: # Equidistant from both integers
        if value > 0:
            return upper
        else:
            return lower
