def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''

    # Convert the string value to float
    float_val = float(value)

    # Check if the float value is already an integer
    if float_val == int(float_val):
        return int(float_val)

    # Calculate the floor and ceiling values of the float
    floor_val = int(float_val) if float_val > 0 else int(float_val) - 1
    ceil_val = int(float_val) + 1 if float_val > 0 else int(float_val)

    # Calculate the differences between the float and the floor/ceiling values
    diff_floor = float_val - floor_val
    diff_ceil = ceil_val - float_val

    # Return the floor or ceiling value based on which is closer
    # If equidistant, return the value farthest from zero
    if diff_floor < diff_ceil:
        return floor_val
    elif diff_ceil < diff_floor:
        return ceil_val
    else:
        return ceil_val if float_val > 0 else floor_val
