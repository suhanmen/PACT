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

    # Convert the input value to a float
    value = float(value)

    # Get the floor and ceil of the float value
    floor_value = int(value // 1)
    ceil_value = int(value // 1 + 1)

    # Calculate the distance from the floor and ceil to the original value
    distance_from_floor = abs(value - floor_value)
    distance_from_ceil = abs(value - ceil_value)

    # Return the closest integer
    if distance_from_floor < distance_from_ceil:
        return floor_value
    elif distance_from_ceil < distance_from_floor:
        return ceil_value
    else:
        if value >= 0:
            return ceil_value
        else:
            return floor_value
