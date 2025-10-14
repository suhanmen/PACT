def closest_integer(value):
    # Convert the input value to a float
    f = float(value)

    # Get the floor and ceiling of the float value
    floor = int(f)
    ceil = int(f + 1)

    # Calculate the distances from the value to the floor and ceiling
    dist_floor = abs(f - floor)
    dist_ceil = abs(ceil - f)

    # If the distance to the floor is smaller or equal to the distance to the ceiling,
    # return the floor. Otherwise, return the ceiling.
    if dist_floor <= dist_ceil:
        return floor
    else:
        return ceil
