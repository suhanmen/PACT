def closest_integer(value):
    # Convert the input value to a float
    num = float(value)

    # Check if the number is already an integer
    if num.is_integer():
        return int(num)

    # Calculate the distance to the nearest integer
    dist_to_floor = num - int(num)
    dist_to_ceil = 1 - dist_to_floor

    # Round the number away from zero if equidistant
    if dist_to_floor == dist_to_ceil:
        return int(abs(num) + 0.5) * (1 if num > 0 else -1)

    # Return the nearest integer
    return int(round(num))
