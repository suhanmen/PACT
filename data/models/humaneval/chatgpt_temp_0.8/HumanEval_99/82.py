def closest_integer(value):
    # Convert the input value to a float
    value = float(value)

    # Check if the value is already an integer
    if value.is_integer():
        return int(value)

    # Calculate the two integers that the value is equidistant from
    lower = int(value - 0.5)
    upper = int(value + 0.5)

    # Calculate the distances between the value and the two integers
    distance_lower = abs(value - lower)
    distance_upper = abs(value - upper)

    # If the value is equidistant from the two integers, round away from zero
    if distance_lower == distance_upper:
        if value > 0:
            return upper
        else:
            return lower

    # Return the closest integer
    if distance_lower < distance_upper:
        return lower
    else:
        return upper
