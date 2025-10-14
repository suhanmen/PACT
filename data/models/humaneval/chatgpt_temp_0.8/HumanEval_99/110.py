def closest_integer(value):
    # Convert the input value to a float
    num = float(value)

    # Check if the value is already an integer, if so return it
    if num.is_integer():
        return int(num)

    # If the value is positive or zero, round up to the nearest integer
    if num >= 0:
        return int(num + 0.5)

    # If the value is negative, round down to the nearest integer
    return int(num - 0.5)
