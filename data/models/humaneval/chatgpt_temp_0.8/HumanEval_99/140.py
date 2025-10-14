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

    # Convert value to a float
    num = float(value)
    
    # Calculate the floor and ceiling of the number
    floor_num = int(num)
    ceil_num = int(num + 1)

    # Calculate the distance between num and the floor and ceiling
    dist_floor = abs(num - floor_num)
    dist_ceil = abs(num - ceil_num)

    # If the distance to the floor is less than or equal to the distance to the ceiling, return the floor
    if dist_floor <= dist_ceil:
        return floor_num
    # Otherwise, return the ceiling
    else:
        return ceil_num
