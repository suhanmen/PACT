def closest_integer(value):
    # Convert the string to a float
    num = float(value)

    # Check if the number is already an integer
    if num.is_integer():
        return int(num)

    # Calculate the distance to the nearest two integers
    dist_lower = abs(num - int(num))
    dist_upper = abs(num - int(num) - 1)

    # Round away from zero if equidistant from two integers
    if dist_lower == dist_upper:
        if num > 0:
            return int(num + 1)
        else:
            return int(num - 1)

    # Return the closest integer
    if dist_lower < dist_upper:
        return int(num)
    else:
        return int(num + 1)
