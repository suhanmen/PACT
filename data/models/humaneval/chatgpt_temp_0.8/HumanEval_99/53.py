def closest_integer(value):
    # Convert the input value to a float
    value = float(value)

    # Extract the integer part of the value
    integer_part = int(value)

    # Calculate the difference between the value and the integer part
    decimal_part = value - integer_part

    # If the decimal part is exactly 0.5 or greater, round up
    if decimal_part >= 0.5:
        return integer_part + 1
    # If the decimal part is exactly -0.5 or lower, round down
    elif decimal_part <= -0.5:
        return integer_part - 1
    # Otherwise, return the closest integer
    else:
        return integer_part
