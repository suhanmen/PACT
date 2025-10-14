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
    num = float(value)
    
    # Get the floor and ceiling of the float
    floor_num = int(num)
    ceil_num = int(num) + 1
    
    # Get the distance from the input value to the floor and ceiling
    distance_to_floor = abs(num - floor_num)
    distance_to_ceil = abs(num - ceil_num)
    
    # Check which integer is closest and return it
    if distance_to_floor < distance_to_ceil:
        return floor_num
    elif distance_to_ceil < distance_to_floor:
        return ceil_num
    else:
        # If the distances are equal, round away from zero
        if num >= 0:
            return ceil_num
        else:
            return floor_num
