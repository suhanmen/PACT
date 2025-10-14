def closest_integer(value):
    # Convert the string value to a float
    value = float(value)
    # Check if the value is already an integer
    if value.is_integer():
        return int(value)
    # Calculate the distance to the nearest integer on either side
    distance_lower = abs(value - int(value))
    distance_upper = abs(int(value) + 1 - value)
    # If the two distances are equal, round away from zero
    if distance_lower == distance_upper:
        return int(value + 0.5 * abs(value) / value)
    # Otherwise, return the closest integer
    elif distance_lower < distance_upper:
        return int(value)
    else:
        return int(value + 1)
