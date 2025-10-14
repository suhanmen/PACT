def closest_integer(value):
    # Convert the value to a float
    value = float(value)

    # Check if the value is already an integer
    if value.is_integer():
        return int(value)

    # Round the value to the nearest integer
    rounded_value = int(round(value))

    # Check if the rounded value is farther from zero than the original value
    if abs(rounded_value - value) < abs(int(value) - value):
        return rounded_value
    else:
        return int(value)
