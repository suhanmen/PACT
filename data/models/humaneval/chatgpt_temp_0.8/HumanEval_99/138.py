def closest_integer(value):
    # Convert the input value to a float
    x = float(value)
    # Compute the floor and ceil of the float
    f, c = int(x), int(x) + 1
    # Compute the distances from the float to the floor and ceil
    dist_f, dist_c = abs(x - f), abs(x - c)
    # If the distances are equal or the float is closer to the floor, return the floor
    if dist_f <= dist_c:
        return f
    # Otherwise, return the ceil
    else:
        return c
