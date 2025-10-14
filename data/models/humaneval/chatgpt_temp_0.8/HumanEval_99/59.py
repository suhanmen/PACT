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
    value_float = float(value)

    # Get the floor and ceiling of the float
    floor = int(value_float // 1)
    ceiling = int(value_float // 1) + 1

    # Calculate the distances from the input value to the floor and ceiling
    distance_floor = abs(value_float - floor)
    distance_ceiling = abs(ceiling - value_float)

    # If the distances are equal, round away from zero
    if distance_floor == distance_ceiling:
        if value_float < 0:
            return ceiling
        else:
            return floor
    # Otherwise, return the closest integer
    elif distance_floor < distance_ceiling:
        return floor
    else:
        return ceiling
