def closest_integer(value):

    # Convert value to a float
    value = float(value)

    # Determine the closest integer to the given value
    closest_int = int(value + 0.5) if value > 0 else int(value - 0.5)

    # Check if the value is equidistant from two integers
    if value - int(value) == 0.5:
        closest_int = int(value) + 1 if value > 0 else int(value) - 1

    # Return the closest integer
    return closest_int
